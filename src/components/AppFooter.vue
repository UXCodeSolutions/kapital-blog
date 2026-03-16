<script setup>
defineProps({
  year: { type: Number, required: true },
});
</script>

<template>
  <footer class="footer" role="contentinfo" id="contacto">
    <div class="container footer-top">
      <div class="footer-brand">
        <router-link to="/" style="text-decoration:none">
          <p class="brand-name">Kapital</p>
        </router-link>
        <p class="muted">Tu dinero, tus reglas</p>
      </div>

      <nav class="footer-nav" aria-label="Enlaces legales">
        <router-link to="/privacidad">Política de Privacidad</router-link>
        <router-link to="/terminos">Términos de Uso</router-link>
        <router-link to="/cookies">Política de Cookies</router-link>
        <router-link to="/contacto">Contacto</router-link>
        <router-link to="/sobre">Sobre Kapital</router-link>
      </nav>
    </div>

    <div class="container footer-bottom">
      <p class="small">© {{ year }} Kapital. Todos los derechos reservados.</p>
    </div>
  </footer>
</template>
