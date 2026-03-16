from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import List, Optional
from datetime import datetime, timedelta
import hashlib, secrets, os

app = FastAPI(title="KapitalBlog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Database Setup ---
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///./blog.db"
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine_kwargs = {}
connect_args = {}
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
elif SQLALCHEMY_DATABASE_URL.startswith("postgresql"):
    connect_args = {"sslmode": "require"}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args, **engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Secret for tokens ---
SECRET_KEY = os.environ.get("SECRET_KEY", "kapital-blog-secret-2026")

# ===================== MODELS =====================

class ArticleModel(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    title = Column(String)
    slug = Column(String, unique=True, index=True, nullable=True)
    description = Column(Text)
    content = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    date = Column(String)
    readTime = Column(String)

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String, default=lambda: datetime.utcnow().isoformat())

class SubscriberModel(Base):
    __tablename__ = "subscribers"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    subscribed_at = Column(String, default=lambda: datetime.utcnow().isoformat())

class ContactModel(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(Text)
    created_at = Column(String, default=lambda: datetime.utcnow().isoformat())

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ===================== HELPERS =====================

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password: str, stored: str) -> bool:
    salt, hashed = stored.split(":")
    return hashlib.sha256((salt + password).encode()).hexdigest() == hashed

def create_token(user_id: int, username: str) -> str:
    """Simple token: base64 of user_id:username:random"""
    import base64
    raw = f"{user_id}:{username}:{secrets.token_hex(16)}"
    return base64.b64encode(raw.encode()).decode()

def slugify(text: str) -> str:
    import re
    text = text.lower().strip()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

# ===================== SCHEMAS =====================

class ArticleBase(BaseModel):
    category: str
    title: str
    description: str
    content: Optional[str] = None
    image_url: Optional[str] = None
    date: str
    readTime: str

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    slug: Optional[str] = None

    model_config = {"from_attributes": True}

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    token: str

class NewsletterSubscribe(BaseModel):
    email: str

class ContactCreate(BaseModel):
    name: str
    email: str
    message: str

class PostAIWebhookPayload(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    seo_score: Optional[int] = None
    word_count: Optional[int] = None
    reading_time: Optional[str] = None
    language: Optional[str] = None
    topic: Optional[str] = None
    published_at: Optional[str] = None

# ===================== API ENDPOINTS =====================

# --- Articles ---

@app.get("/articles", response_model=List[ArticleResponse])
def read_articles(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(ArticleModel)
    if category:
        query = query.filter(ArticleModel.category == category)
    if q:
        search = f"%{q}%"
        query = query.filter(
            (ArticleModel.title.ilike(search)) |
            (ArticleModel.description.ilike(search)) |
            (ArticleModel.content.ilike(search))
        )
    articles = query.order_by(ArticleModel.id.desc()).offset(skip).limit(limit).all()
    return articles

@app.get("/articles/{article_id}", response_model=ArticleResponse)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return article

@app.post("/articles", response_model=ArticleResponse)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    slug = slugify(article.title)
    existing = db.query(ArticleModel).filter(ArticleModel.slug == slug).first()
    if existing:
        slug = f"{slug}-{secrets.token_hex(3)}"
    db_article = ArticleModel(**article.dict(), slug=slug)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/categories", response_model=List[dict])
def get_categories(db: Session = Depends(get_db)):
    from sqlalchemy import func
    results = db.query(ArticleModel.category, func.count(ArticleModel.id)).group_by(ArticleModel.category).all()
    return [{"label": cat, "count": count} for cat, count in results]

# --- Auth ---

@app.post("/auth/register", response_model=UserResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing = db.query(UserModel).filter(
        (UserModel.email == user.email) | (UserModel.username == user.username)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email o usuario ya registrado")
    db_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_token(db_user.id, db_user.username)
    return UserResponse(id=db_user.id, username=db_user.username, email=db_user.email, token=token)

@app.post("/auth/login", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = create_token(db_user.id, db_user.username)
    return UserResponse(id=db_user.id, username=db_user.username, email=db_user.email, token=token)

# --- Newsletter ---

@app.post("/newsletter/subscribe")
def subscribe_newsletter(data: NewsletterSubscribe, db: Session = Depends(get_db)):
    existing = db.query(SubscriberModel).filter(SubscriberModel.email == data.email).first()
    if existing:
        return {"message": "Ya estás suscrito", "status": "already_subscribed"}
    sub = SubscriberModel(email=data.email)
    db.add(sub)
    db.commit()
    return {"message": "¡Suscripción exitosa!", "status": "subscribed"}

# --- Contact ---

@app.post("/contact")
def create_contact(data: ContactCreate, db: Session = Depends(get_db)):
    contact = ContactModel(name=data.name, email=data.email, message=data.message)
    db.add(contact)
    db.commit()
    return {"message": "Mensaje recibido. Te contactaremos pronto.", "status": "sent"}

# --- PostAI Webhook ---

@app.post("/webhook/postai", response_model=ArticleResponse)
def create_article_from_postai(payload: PostAIWebhookPayload, db: Session = Depends(get_db)):
    date_str = payload.published_at.split("T")[0] if payload.published_at else datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(payload.title)
    existing = db.query(ArticleModel).filter(ArticleModel.slug == slug).first()
    if existing:
        slug = f"{slug}-{secrets.token_hex(3)}"

    article_data = {
        "category": payload.topic or "Sin categoría",
        "title": payload.title,
        "description": payload.content[:200] + "..." if len(payload.content) > 200 else payload.content,
        "content": payload.content,
        "image_url": payload.image_url,
        "date": date_str,
        "readTime": payload.reading_time or "5 min",
        "slug": slug,
    }
    db_article = ArticleModel(**article_data)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# ===================== SEED DATA =====================

def seed_database(db: Session):
    if db.query(ArticleModel).first() is None:
        initial_articles = [
            {
                "category": "Presupuesto",
                "title": "El método 50/30/20 explicado con un ejemplo real",
                "slug": "metodo-50-30-20-ejemplo-real",
                "description": "Crea un presupuesto simple, flexible y fácil de mantener con categorías claras y reglas prácticas.",
                "content": """<p>El método 50/30/20 es una de las reglas más populares para organizar tus finanzas personales. Fue popularizada por la senadora Elizabeth Warren en su libro <em>All Your Worth</em>, y su simplicidad la convierte en un punto de partida ideal para cualquier persona que quiera tomar control de su dinero.</p>

<h2>¿Cómo funciona?</h2>
<p>Divide tus ingresos netos (después de impuestos) en tres grandes categorías:</p>
<ul>
<li><strong>50% — Necesidades:</strong> Alquiler, servicios, comida, transporte, seguros y pagos mínimos de deudas.</li>
<li><strong>30% — Deseos:</strong> Entretenimiento, restaurantes, suscripciones, viajes y compras no esenciales.</li>
<li><strong>20% — Ahorro e inversión:</strong> Fondo de emergencia, inversiones, pagos extra de deuda.</li>
</ul>

<h2>Ejemplo práctico</h2>
<p>Imaginemos que ganas $3,000 al mes después de impuestos:</p>
<ul>
<li><strong>Necesidades ($1,500):</strong> $900 alquiler + $150 servicios + $300 comida + $150 transporte</li>
<li><strong>Deseos ($900):</strong> $200 entretenimiento + $100 gimnasio + $300 restaurantes + $300 compras</li>
<li><strong>Ahorro ($600):</strong> $300 fondo de emergencia + $300 inversiones</li>
</ul>

<h2>Consejos para empezar</h2>
<p>No necesitas ser perfecto desde el primer mes. Empieza rastreando tus gastos durante 30 días para entender a dónde va tu dinero. Luego ajusta gradualmente hasta acercarte a la distribución 50/30/20.</p>

<p>Herramientas como apps de presupuesto o una simple hoja de cálculo pueden hacer toda la diferencia. Lo importante es la consistencia, no la perfección.</p>""",
                "image_url": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=800",
                "date": "2026-03-06",
                "readTime": "6 min"
            },
            {
                "category": "Ahorro",
                "title": "Ahorro automático: el sistema que funciona incluso cuando no tienes motivación",
                "slug": "ahorro-automatico-sistema",
                "description": "Cómo configurar transferencias, prioridades y un fondo de emergencia sin fricción.",
                "content": """<p>La motivación es un recurso volátil. Hay días en los que te sientes invencible con tus finanzas, y otros en los que un impulso en Amazon arruina todo. La solución no es más motivación — es automatización.</p>

<h2>El principio de "págate a ti mismo primero"</h2>
<p>En vez de ahorrar lo que sobra al final del mes (spoiler: nunca sobra nada), configura transferencias automáticas que muevan dinero a tu cuenta de ahorro el mismo día que recibes tu salario.</p>

<h2>Cómo configurarlo paso a paso</h2>
<ol>
<li><strong>Abre una cuenta de ahorro separada</strong> — idealmente en un banco diferente para reducir la tentación.</li>
<li><strong>Define un porcentaje fijo</strong> — empieza con el 10% de tu ingreso neto si el 20% se siente agresivo.</li>
<li><strong>Programa la transferencia automática</strong> — el mismo día que recibes tu nómina.</li>
<li><strong>Olvídate de que existe</strong> — ese dinero no está disponible para gastos.</li>
</ol>

<h2>Fondo de emergencia: tu primera meta</h2>
<p>Antes de invertir o pagar deudas agresivamente, construye un colchón de 3 a 6 meses de gastos esenciales. Este fondo te protege de imprevistos sin recurrir a tarjetas de crédito.</p>

<p>Recuerda: el mejor plan financiero es el que funciona sin que tengas que pensar en él cada día.</p>""",
                "image_url": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=800",
                "date": "2026-03-02",
                "readTime": "5 min"
            },
            {
                "category": "Inversión",
                "title": "DCA sin estrés: invertir con disciplina en mercados volátiles",
                "slug": "dca-sin-estres-mercados-volatiles",
                "description": "Una estrategia simple para invertir de forma periódica, reducir ansiedad y pensar a largo plazo.",
                "content": """<p>Dollar Cost Averaging (DCA) es la estrategia más amigable para inversores que no quieren obsesionarse con el timing del mercado. La premisa es simple: inviertes una cantidad fija en intervalos regulares, sin importar el precio.</p>

<h2>¿Por qué funciona?</h2>
<p>Cuando el mercado baja, tu dinero compra más participaciones. Cuando sube, compras menos. Con el tiempo, el costo promedio tiende a suavizarse, eliminando la presión de "comprar en el momento perfecto".</p>

<h2>Ejemplo con ETFs</h2>
<p>Supongamos que inviertes $200 al mes en un ETF del S&P 500:</p>
<ul>
<li><strong>Mes 1:</strong> Precio $50 → compras 4 participaciones</li>
<li><strong>Mes 2:</strong> Precio $40 → compras 5 participaciones</li>
<li><strong>Mes 3:</strong> Precio $60 → compras 3.33 participaciones</li>
</ul>
<p>En 3 meses invertiste $600 y tienes 12.33 participaciones a un costo promedio de $48.66.</p>

<h2>Claves para el éxito</h2>
<ul>
<li>Elige un activo diversificado (ETFs son ideales para principiantes).</li>
<li>Automatiza las compras mensuales.</li>
<li>No mires el portafolio cada día — revisa trimestralmente.</li>
<li>Piensa en horizonte de 5+ años.</li>
</ul>

<p>El DCA no te hará millonario de la noche a la mañana, pero te protege de errores emocionales que destruyen portafolios.</p>""",
                "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=800",
                "date": "2026-02-25",
                "readTime": "7 min"
            },
            {
                "category": "Crédito",
                "title": "Tarjetas de crédito: 7 reglas para evitar intereses y mejorar tu score",
                "slug": "tarjetas-credito-7-reglas",
                "description": "Aprende a usar crédito a tu favor con pagos inteligentes, límites y hábitos medibles.",
                "content": """<p>Las tarjetas de crédito no son el enemigo. El problema es usarlas sin estrategia. Bien utilizadas, pueden mejorar tu historial crediticio, darte cashback y proteger tus compras. Mal utilizadas... ya sabes lo que pasa.</p>

<h2>Las 7 reglas de oro</h2>

<h3>1. Nunca gastes más de lo que puedes pagar este mes</h3>
<p>Si no puedes pagarlo en efectivo, no lo pongas en la tarjeta. Así de simple.</p>

<h3>2. Paga el total, no el mínimo</h3>
<p>El pago mínimo es una trampa diseñada para que pagues intereses durante años. Siempre paga el saldo completo.</p>

<h3>3. Mantén tu utilización bajo el 30%</h3>
<p>Si tu límite es $10,000, no uses más de $3,000. Tu score crediticio te lo agradecerá.</p>

<h3>4. Configura pagos automáticos</h3>
<p>Un solo pago atrasado puede dañar tu score durante meses. Automatiza el pago total.</p>

<h3>5. No abras tarjetas solo por las promociones</h3>
<p>Cada solicitud genera un "hard inquiry" que baja tu score temporalmente.</p>

<h3>6. Revisa tus estados de cuenta</h3>
<p>Detecta cargos fraudulentos o suscripciones olvidadas cada mes.</p>

<h3>7. Usa las recompensas estratégicamente</h3>
<p>Cashback en compras que ya ibas a hacer. No compres de más solo por los puntos.</p>""",
                "image_url": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=800",
                "date": "2026-02-18",
                "readTime": "8 min"
            },
            {
                "category": "Ahorro",
                "title": "Fondo de emergencia: cuánto necesitas y cómo construirlo",
                "slug": "fondo-emergencia-cuanto-como",
                "description": "Define metas por etapas y evita que imprevistos rompan tu presupuesto.",
                "content": """<p>Un fondo de emergencia es la base de cualquier plan financiero sólido. Sin él, un gasto inesperado — una reparación del auto, una visita al hospital, o la pérdida de empleo — puede descarrilar meses de progreso financiero.</p>

<h2>¿Cuánto necesitas?</h2>
<p>La recomendación estándar es de 3 a 6 meses de gastos esenciales. Pero no tienes que llegar ahí de golpe.</p>

<h3>Etapas del fondo de emergencia</h3>
<ul>
<li><strong>Etapa 1 — $1,000:</strong> Un mini-colchón para imprevistos menores.</li>
<li><strong>Etapa 2 — 1 mes de gastos:</strong> Cubre lo básico si pierdes ingresos temporalmente.</li>
<li><strong>Etapa 3 — 3 meses:</strong> Tranquilidad real. Puedes buscar empleo sin desesperación.</li>
<li><strong>Etapa 4 — 6 meses:</strong> Libertad financiera defensiva completa.</li>
</ul>

<h2>Dónde guardarlo</h2>
<p>Tu fondo de emergencia debe ser <strong>líquido</strong> (accesible en 24-48 horas) y <strong>seguro</strong> (no en acciones ni cripto). Las mejores opciones:</p>
<ul>
<li>Cuenta de ahorro de alto rendimiento</li>
<li>Certificados de depósito a corto plazo</li>
<li>Cuentas del mercado monetario</li>
</ul>

<p>La regla más importante: este dinero es solo para emergencias reales. Unas vacaciones o un iPhone nuevo no son emergencias.</p>""",
                "image_url": "https://images.unsplash.com/photo-1633158829585-23ba8f7c8caf?q=80&w=800",
                "date": "2026-02-10",
                "readTime": "6 min"
            },
            {
                "category": "Inversión",
                "title": "ETF vs acciones: cómo elegir sin complicarte",
                "slug": "etf-vs-acciones-como-elegir",
                "description": "Diferencias clave, riesgos y una guía rápida para principiantes.",
                "content": """<p>Si estás empezando a invertir, probablemente te preguntas: ¿debería comprar acciones individuales o ETFs? La respuesta depende de tu experiencia, tu tiempo disponible y tu tolerancia al riesgo.</p>

<h2>¿Qué es un ETF?</h2>
<p>Un ETF (Exchange-Traded Fund) es un fondo que agrupa múltiples activos — como acciones, bonos o materias primas — y se negocia en bolsa como una acción individual. Un solo ETF del S&P 500 te da exposición a las 500 empresas más grandes de EE.UU.</p>

<h2>ETFs vs Acciones: comparación rápida</h2>

<table>
<tr><th>Criterio</th><th>ETFs</th><th>Acciones individuales</th></tr>
<tr><td>Diversificación</td><td>Alta (automática)</td><td>Baja (debes diversificar tú)</td></tr>
<tr><td>Riesgo</td><td>Menor</td><td>Mayor</td></tr>
<tr><td>Conocimiento necesario</td><td>Básico</td><td>Avanzado</td></tr>
<tr><td>Tiempo de investigación</td><td>Mínimo</td><td>Alto</td></tr>
<tr><td>Potencial de retorno</td><td>Moderado</td><td>Alto (con más riesgo)</td></tr>
</table>

<h2>¿Cuándo elegir acciones individuales?</h2>
<p>Solo si tienes el tiempo y conocimiento para analizar estados financieros, entender valuaciones y tolerar alta volatilidad. Incluso los profesionales pierden dinero eligiendo acciones.</p>

<h2>Recomendación para principiantes</h2>
<p>Empieza con ETFs diversificados (como VOO, VTI o IWDA) usando DCA. Una vez que entiendas el mercado y tengas un portafolio base sólido, puedes destinar un 10-20% a acciones individuales que conozcas bien.</p>""",
                "image_url": "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?q=80&w=800",
                "date": "2026-02-03",
                "readTime": "6 min"
            }
        ]
        for article_data in initial_articles:
            db_article = ArticleModel(**article_data)
            db.add(db_article)
        db.commit()

# Seed on startup
with SessionLocal() as db:
    seed_database(db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
