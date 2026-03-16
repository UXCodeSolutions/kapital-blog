<script setup>
const emit = defineEmits(['navigate']);

const go = (id) => emit('navigate', id);
</script>

<template>
  <section class="hero-architecture" aria-label="Sección principal">
    <div class="hero-bg-wrapper">
      <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=2940&auto=format&fit=crop" alt="Global Financial Markets" class="hero-bg-img" />
      <div class="hero-overlay"></div>
    </div>
    
    <div class="container hero-content">
      <div class="hero-tag">Markets</div>
      <h1 class="hero-title">Navigating Volatility:<br/>The Future of<br/>Global Markets</h1>
      <p class="hero-lead">
        Exploring how institutional investors and modern traders are adapting their portfolios to shifting geopolitical landscapes and rising interest rates.
      </p>
      
      <div class="hero-meta-author">
        <div class="author-avatar">
          <img src="https://i.pravatar.cc/100?img=5" alt="Elena Vance" />
        </div>
        <span class="author-name">Elena Vance</span>
        <span class="meta-dot">·</span>
        <span class="meta-date">Oct 24, 2023</span>
        <span class="meta-dot">·</span>
        <span class="meta-read-time">8 min read</span>
      </div>
      
      <div class="hero-actions">
        <a class="btn-read-article" href="#" @click.prevent="go('articulos')">Read Article</a>
      </div>
    </div>
  </section>
</template>
