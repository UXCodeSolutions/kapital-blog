<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const email = ref('');
const password = ref('');
const error = ref('');
const isLoading = ref(false);

const API = 'http://localhost:8000';

const handleLogin = async () => {
  error.value = '';
  if (!email.value || !password.value) {
    error.value = 'Por favor completa todos los campos';
    return;
  }
  isLoading.value = true;
  try {
    const res = await fetch(`${API}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Error al iniciar sesión');
    localStorage.setItem('kapital-token', data.token);
    localStorage.setItem('kapital-user', JSON.stringify({ id: data.id, username: data.username, email: data.email }));
    router.push('/');
  } catch (e) {
    error.value = e.message;
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <main class="site-main auth-view">
    <div class="container auth-container">
      <div class="auth-card">
        <div class="auth-header">
          <h1>Iniciar Sesión</h1>
          <p>Accede a tu cuenta de Kapital</p>
        </div>

        <form @submit.prevent="handleLogin" class="auth-form">
          <div class="form-group">
            <label for="email">Email</label>
            <input id="email" v-model="email" type="email" placeholder="tu@email.com" autocomplete="email" />
          </div>
          <div class="form-group">
            <label for="password">Contraseña</label>
            <input id="password" v-model="password" type="password" placeholder="••••••••" autocomplete="current-password" />
          </div>

          <div v-if="error" class="auth-error">{{ error }}</div>

          <button type="submit" class="btn-auth" :disabled="isLoading">
            {{ isLoading ? 'Entrando...' : 'Iniciar Sesión' }}
          </button>
        </form>

        <p class="auth-switch">
          ¿No tienes cuenta? <router-link to="/registro">Regístrate aquí</router-link>
        </p>
      </div>
    </div>
  </main>
</template>

<style scoped>
.auth-view { padding: 80px 0; }
.auth-container { display: flex; justify-content: center; }
.auth-card {
  width: 100%; max-width: 440px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 48px 40px;
  box-shadow: var(--shadow);
}
.auth-header { text-align: center; margin-bottom: 32px; }
.auth-header h1 { font-size: 28px; font-weight: 800; margin: 0 0 8px; }
.auth-header p { color: var(--muted); margin: 0; }
.auth-form { display: flex; flex-direction: column; gap: 20px; }
.form-group { display: flex; flex-direction: column; gap: 6px; }
.form-group label { font-size: 14px; font-weight: 600; }
.form-group input {
  padding: 12px 16px; border-radius: 10px;
  border: 1px solid var(--border); background: var(--bg);
  font-size: 16px; color: var(--text); transition: border-color 0.2s;
}
.form-group input:focus { outline: none; border-color: var(--purple); }
.auth-error {
  background: #FEF2F2; border: 1px solid #FECACA; color: #DC2626;
  padding: 10px 14px; border-radius: 8px; font-size: 14px;
}
.btn-auth {
  background: var(--purple); color: white; border: none;
  padding: 14px; border-radius: 10px; font-size: 16px; font-weight: 700;
  cursor: pointer; transition: background 0.2s;
}
.btn-auth:hover { background: var(--purple-2); }
.btn-auth:disabled { opacity: 0.6; cursor: not-allowed; }
.auth-switch { text-align: center; margin-top: 20px; color: var(--muted); font-size: 14px; }
.auth-switch a { color: var(--purple); font-weight: 600; }
</style>
