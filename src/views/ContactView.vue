<script setup>
import { ref } from 'vue';

const name = ref('');
const email = ref('');
const message = ref('');
const status = ref('');
const isError = ref(false);
const isLoading = ref(false);

const API = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '');

const handleSubmit = async () => {
  status.value = '';
  isError.value = false;
  if (!name.value || !email.value || !message.value) {
    status.value = 'Please fill in all fields';
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
    if (!res.ok) throw new Error(data.detail || 'Error sending message');
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
        <h1>Contact Us</h1>
        <p>Have a question, suggestion, or collaboration idea? We'd love to hear from you.</p>
        <div class="contact-details">
          <div class="detail-item">
            <span class="detail-icon" aria-hidden="true">
              <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 6h16v12H4z" />
                <path d="m4 7 8 6 8-6" />
              </svg>
            </span>
            <div>
              <strong>Email</strong>
              <p>contact@kapital.blog</p>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon" aria-hidden="true">
              <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="9" />
                <path d="M12 7v6l3 2" />
              </svg>
            </span>
            <div>
              <strong>Response Time</strong>
              <p>We reply within 24-48 hours</p>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon" aria-hidden="true">
              <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 21s7-4.5 7-10a7 7 0 0 0-14 0c0 5.5 7 10 7 10z" />
                <circle cx="12" cy="11" r="2" />
              </svg>
            </span>
            <div>
              <strong>Social Media</strong>
              <p>@KapitalBlog on all platforms</p>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-card">
        <form @submit.prevent="handleSubmit" class="contact-form">
          <div class="form-group">
            <label for="name">Name</label>
            <input id="name" v-model="name" type="text" placeholder="Your full name" />
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input id="email" v-model="email" type="email" placeholder="you@email.com" />
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" v-model="message" rows="5" placeholder="Write your message here..."></textarea>
          </div>

          <div v-if="status" :class="['form-status', isError ? 'error' : 'success']">{{ status }}</div>

          <button type="submit" class="btn-contact" :disabled="isLoading">
            {{ isLoading ? 'Sending...' : 'Send Message' }}
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
