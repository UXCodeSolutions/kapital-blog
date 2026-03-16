<script setup>
import { ref } from 'vue';

const name = ref('');
const email = ref('');
const message = ref('');
const status = ref('');
const isError = ref(false);
const isLoading = ref(false);

const API = 'http://localhost:8000';

const handleSubmit = async () => {
  status.value = '';
  isError.value = false;
  if (!name.value || !email.value || !message.value) {
    status.value = 'Por favor completa todos los campos';
    isError.value = true;
    return;
  }
  isLoading.value = true;
  try {
    const res = await fetch(`${API}/contact`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name.value, email: email.value, message: message.value })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Error al enviar');
    status.value = data.message;
    isError.value = false;
    name.value = '';
    email.value = '';
    message.value = '';
  } catch (e) {
    status.value = e.message;
    isError.value = true;
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <main class="site-main contact-view">
    <div class="container contact-container">
      <div class="contact-info">
        <h1>Contáctanos</h1>
        <p>¿Tienes alguna pregunta, sugerencia o propuesta de colaboración? Nos encantaría escucharte.</p>
        <div class="contact-details">
          <div class="detail-item">
            <span class="detail-icon">✉️</span>
            <div>
              <strong>Email</strong>
              <p>contacto@kapital.blog</p>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">🕐</span>
            <div>
              <strong>Tiempo de respuesta</strong>
              <p>Respondemos en 24-48 horas</p>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">📍</span>
            <div>
              <strong>Redes sociales</strong>
              <p>@KapitalBlog en todas las plataformas</p>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-card">
        <form @submit.prevent="handleSubmit" class="contact-form">
          <div class="form-group">
            <label for="name">Nombre</label>
            <input id="name" v-model="name" type="text" placeholder="Tu nombre completo" />
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input id="email" v-model="email" type="email" placeholder="tu@email.com" />
          </div>
          <div class="form-group">
            <label for="message">Mensaje</label>
            <textarea id="message" v-model="message" rows="5" placeholder="Escribe tu mensaje aquí..."></textarea>
          </div>

          <div v-if="status" :class="['form-status', isError ? 'error' : 'success']">{{ status }}</div>

          <button type="submit" class="btn-contact" :disabled="isLoading">
            {{ isLoading ? 'Enviando...' : 'Enviar Mensaje' }}
          </button>
        </form>
      </div>
    </div>
  </main>
</template>

<style scoped>
.contact-view { padding: 80px 0; }
.contact-container {
  display: grid; grid-template-columns: 1fr 1fr; gap: 60px;
  align-items: start; max-width: 1000px; margin: 0 auto;
}
.contact-info h1 { font-size: 36px; font-weight: 800; margin: 0 0 16px; letter-spacing: -1px; }
.contact-info > p { color: var(--muted); font-size: 18px; line-height: 1.6; margin: 0 0 40px; }

.contact-details { display: flex; flex-direction: column; gap: 24px; }
.detail-item { display: flex; gap: 16px; align-items: flex-start; }
.detail-icon { font-size: 24px; min-width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; }
.detail-item strong { display: block; font-size: 14px; margin-bottom: 2px; }
.detail-item p { margin: 0; color: var(--muted); font-size: 14px; }

.contact-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 40px;
  box-shadow: var(--shadow);
}
.contact-form { display: flex; flex-direction: column; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group label { font-size: 14px; font-weight: 600; }
.form-group input, .form-group textarea {
  padding: 12px 16px; border-radius: 10px;
  border: 1px solid var(--border); background: var(--bg);
  font-size: 16px; color: var(--text); transition: border-color 0.2s;
  font-family: inherit; resize: vertical;
}
.form-group input:focus, .form-group textarea:focus { outline: none; border-color: var(--purple); }

.form-status { padding: 10px 14px; border-radius: 8px; font-size: 14px; }
.form-status.success { background: #F0FDF4; border: 1px solid #BBF7D0; color: #16A34A; }
.form-status.error { background: #FEF2F2; border: 1px solid #FECACA; color: #DC2626; }

.btn-contact {
  background: var(--purple); color: white; border: none;
  padding: 14px; border-radius: 10px; font-size: 16px; font-weight: 700;
  cursor: pointer; transition: background 0.2s;
}
.btn-contact:hover { background: var(--purple-2); }
.btn-contact:disabled { opacity: 0.6; cursor: not-allowed; }

@media (max-width: 768px) {
  .contact-container { grid-template-columns: 1fr; gap: 40px; }
}
</style>
