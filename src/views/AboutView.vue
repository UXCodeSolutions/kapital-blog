<template>
  <main class="site-main about-view">
    <div class="container about-container">
      <section class="about-hero">
        <h1>Sobre Kapital</h1>
        <p class="about-lead">El pulso diario del mundo financiero, económico y de negocios. Sin filtros, sin intermediarios.</p>
      </section>

      <section class="about-content">
        <div class="about-block">
          <h2>Nuestra Misión</h2>
          <p>KapitalBlog es un portal digital independiente y periodístico cuyo único objetivo es informar. Curamos y analizamos las noticias más relevantes de la macroeconomía, los mercados de valores, bienes raíces, tecnología financiera y adopción digital para mantenerte al día con el flujo global del capital.</p>
          <p>No ofrecemos servicios financieros, no impartimos estrategias comerciales, ni proveemos recomendaciones de inversión de ningún tipo. Somos observadores del mercado que traducen la complejidad corporativa en piezas de lectura claras y accesibles.</p>
        </div>

        <div class="about-block">
          <h2>¿Qué Cubrimos?</h2>
          <div class="topics-grid">
            <div class="topic-card">
              <span class="topic-icon">💰</span>
              <h3>Presupuesto</h3>
              <p>Noticias sobre políticas fiscales, presupuestos gubernamentales y flujos de capital</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon">🏦</span>
              <h3>Ahorro</h3>
              <p>Tendencias en tasas de interés, productos bancarios y movimientos del sector</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon">📈</span>
              <h3>Inversión</h3>
              <p>Cobertura de mercados bursátiles, criptomonedas y activos alternativos</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon">💳</span>
              <h3>Crédito</h3>
              <p>Análisis del panorama crediticio, regulaciones y productos financieros</p>
            </div>
          </div>
        </div>

        <div class="about-block">
          <h2>Nuestro Enfoque</h2>
          <p>Operamos como una sala de redacción colaborativa y descentralizada. La información es más grande que cualquier individuo y, por ende, publicamos bajo el sello editorial único de Kapital, garantizando que el protagonista sea siempre la noticia, los datos y las historias, no la persona que las redacta.</p>
          <ul class="principles-list">
            <li><strong>Claridad sobre jerga:</strong> Reducimos conceptos complejos sin simplificarlos excesivamente.</li>
            <li><strong>Independencia basada en datos:</strong> Nuestros análisis se basan en métricas empíricas verificables.</li>
            <li><strong>Solo noticias:</strong> No damos consejos financieros ni recomendaciones de inversión.</li>
          </ul>
        </div>

        <div class="about-block about-cta">
          <h2>¿Deseas ponerte en contacto?</h2>
          <p>Para notas de prensa, correcciones o consultas generales a nuestra mesa de redacción.</p>
          <router-link to="/contacto" class="btn-cta">Contáctanos →</router-link>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.about-view { padding: 60px 0 80px; }
.about-container { max-width: 860px; margin: 0 auto; }

.about-hero { text-align: center; margin-bottom: 60px; }
.about-hero h1 { font-size: 44px; font-weight: 800; letter-spacing: -1px; margin: 0 0 16px; }
.about-lead { font-size: 20px; color: var(--muted); line-height: 1.6; max-width: 600px; margin: 0 auto; }

.about-content { display: flex; flex-direction: column; gap: 48px; }
.about-block h2 { font-size: 24px; font-weight: 800; margin: 0 0 16px; letter-spacing: -0.5px; }
.about-block p { color: var(--muted); font-size: 16px; line-height: 1.7; margin: 0 0 12px; }

.topics-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 20px; }
.topic-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
  padding: 24px; transition: transform 0.2s;
}
.topic-card:hover { transform: translateY(-2px); }
.topic-icon { font-size: 32px; display: block; margin-bottom: 12px; }
.topic-card h3 { font-size: 18px; margin: 0 0 8px; }
.topic-card p { color: var(--muted); font-size: 14px; margin: 0; }

.principles-list { list-style: none; padding: 0; margin-top: 16px; }
.principles-list li {
  margin-bottom: 16px; font-size: 16px; line-height: 1.7; color: var(--muted);
  border-left: 3px solid var(--purple); padding-left: 16px;
}

.about-cta { text-align: center; background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 48px 24px; }
.btn-cta {
  display: inline-block; background: var(--purple); color: white; padding: 14px 28px;
  border-radius: 10px; font-weight: 700; font-size: 16px; margin-top: 8px;
  transition: background 0.2s; text-decoration: none;
}
.btn-cta:hover { background: var(--purple-2); text-decoration: none; }

@media (max-width: 768px) {
  .topics-grid { grid-template-columns: 1fr; }
}
</style>
