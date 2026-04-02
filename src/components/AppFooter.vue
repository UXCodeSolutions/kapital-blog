<script setup>
defineProps({
  year: { type: Number, required: true },
});
</script>

<template>
  <footer class="footer" role="contentinfo" id="contact">
    <div class="container footer-top">
      <div class="footer-brand">
        <router-link to="/" style="text-decoration:none">
          <p class="brand-name">Kapital</p>
        </router-link>
        <p class="muted">Your money, your rules</p>
      </div>

      <nav class="footer-nav" aria-label="Legal links">
        <router-link to="/privacy">Privacy Policy</router-link>
        <router-link to="/terms">Terms of Use</router-link>
        <router-link to="/cookies">Cookie Policy</router-link>
        <router-link to="/contact">Contact</router-link>
        <router-link to="/about">About Kapital</router-link>
      </nav>
    </div>

    <div class="container footer-bottom">
      <p class="small">© {{ year }} Kapital. All rights reserved.</p>
    </div>
  </footer>
</template>
