<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue';

const props = defineProps({
  articles: {
    type: Array,
    required: true
  }
});

const recentArticles = computed(() => props.articles.slice(0, 5));
const currentIndex = ref(0);
let intervalId = null;

const nextSlide = () => {
  if (recentArticles.value.length === 0) return;
  currentIndex.value = (currentIndex.value + 1) % recentArticles.value.length;
};

const goToSlide = (index) => {
  currentIndex.value = index;
  resetInterval();
};

const resetInterval = () => {
  if (intervalId) clearInterval(intervalId);
  intervalId = setInterval(nextSlide, 3000);
};

onMounted(() => {
  resetInterval();
});

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId);
});

const emit = defineEmits(['navigate']);
</script>

<template>
  <div class="dynamic-hero-container" v-if="recentArticles.length > 0">
    <div 
      class="dynamic-slide" 
      v-for="(article, index) in recentArticles" 
      :key="article.id"
      :class="{ active: index === currentIndex }"
    >
      <div class="hero-bg-wrapper">
        <div class="hero-bg-img img" :data-img="article.imgKey"></div>
        <div class="hero-overlay"></div>
      </div>
      
      <div class="container hero-content">
        <div class="hero-tag" style="background: var(--purple); color: white; border: none; align-self: flex-start; padding: 4px 12px; border-radius: 4px; font-weight: 600; font-size: 12px; text-transform: uppercase;">
          {{ article.category }}
        </div>
        
        <h1 class="hero-title">{{ article.title }}</h1>
        <p class="hero-lead">{{ article.description || 'Explora nuestras últimas perspectivas y noticias del mercado global.' }}</p>
        
        <div class="hero-meta-author">
          <span class="meta-date">{{ article.date }}</span>
          <span class="meta-dot">·</span>
          <span class="meta-read-time">{{ article.readTime }}</span>
        </div>
        
        <div class="hero-actions">
          <router-link :to="'/articulo/' + article.id" class="btn-read-article">Read Article</router-link>
        </div>
      </div>
    </div>
    
    <div class="hero-indicators">
      <div 
        v-for="(_, index) in recentArticles" 
        :key="'dot-'+index"
        class="indicator-dot"
        :class="{ active: index === currentIndex }"
        @click="goToSlide(index)"
      ></div>
    </div>
  </div>
</template>

<style scoped>
.dynamic-hero-container {
  position: relative;
  width: 100%;
  height: 80vh;
  min-height: 600px;
  max-height: 800px;
  background: var(--bg);
  overflow: hidden;
}

.dynamic-slide {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0;
  transition: opacity 0.8s ease-in-out;
  pointer-events: none;
  display: flex;
  align-items: center;
}

.dynamic-slide.active {
  opacity: 1;
  pointer-events: auto;
  z-index: 2;
}

.hero-bg-wrapper {
  position: absolute;
  inset: 0;
  z-index: -1;
}

.hero-bg-img {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(10,10,12,0.95) 0%, rgba(10,10,12,0.6) 50%, rgba(10,10,12,0.2) 100%);
}

.hero-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-width: 800px;
  position: relative;
  z-index: 10;
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -2px;
  color: #fff;
  margin: 0;
}

.hero-lead {
  font-size: 1.25rem;
  line-height: 1.6;
  color: rgba(255,255,255,0.8);
  max-width: 600px;
  margin: 0;
}

.hero-meta-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: rgba(255,255,255,0.7);
  font-size: 0.95rem;
}

.hero-actions {
  margin-top: 1rem;
}

.btn-read-article {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  color: var(--bg);
  padding: 1rem 2rem;
  font-weight: 600;
  border-radius: 4px;
  text-decoration: none;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.btn-read-article:hover {
  background: var(--purple);
  color: #fff;
  transform: translateY(-2px);
}

.hero-indicators {
  position: absolute;
  bottom: 30px;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 12px;
  z-index: 20;
}

.indicator-dot {
  width: 40px;
  height: 4px;
  background: rgba(255,255,255,0.3);
  cursor: pointer;
  transition: background 0.3s;
}

.indicator-dot.active {
  background: #fff;
}

@media (max-width: 768px) {
  .hero-overlay {
    background: linear-gradient(to bottom, rgba(10,10,12,0.4) 0%, rgba(10,10,12,0.95) 100%);
  }
  .dynamic-slide {
    align-items: flex-end;
    padding-bottom: 80px;
  }
}
</style>
