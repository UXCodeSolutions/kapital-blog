<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const article = ref(null);
const isLoading = ref(true);

const API = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '');

const imgKeys = ['typography', 'remote', 'smarthome', 'travel', 'mindfulness', 'web3'];


const fetchArticle = async () => {
  try {
    const id = route.params.id;
    const response = await fetch(`${API}/articles/${id}`);
    if (!response.ok) throw new Error('Error Loading Article');
    const data = await response.json();
    
    // Enrich with display data
    data.imgKey = imgKeys[(data.id - 1) % imgKeys.length];
    article.value = data;
  } catch (error) {
    console.error('Error:', error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchArticle();
});
</script>

<template>
  <main class="site-main article-view">
    <div class="container" v-if="isLoading" style="padding: 4rem 2rem; text-align: center; color: var(--muted);">
      Loading article...
    </div>
    
    <template v-else-if="article">
      <!-- Hero Image -->
      <div class="article-hero" v-if="article.image_url">
        <img :src="article.image_url" :alt="article.title" class="article-hero-img" />
        <div class="article-hero-overlay"></div>
      </div>

      <div class="container article-body">
        <span class="card-badge">{{ article.category }}</span>
        <h1 class="article-title">{{ article.title }}</h1>
        
        <div class="article-meta-bar">
          <div class="meta-details">Published on {{ article.date }} · ⏱ {{ article.readTime }} read</div>
        </div>

        <div class="article-layout-grid">
          <!-- Left Sidebar -->
          <aside class="article-sidebar sidebar-left">
            <div class="ad-skyscraper">Advertisement block</div>
          </aside>
          
          <!-- Article Content -->
          <div class="article-main-content">
            <div class="article-content" v-if="article.content">
              <div v-html="article.content"></div>
            </div>
            <div class="article-content" v-else>
              <p>{{ article.description }}</p>
            </div>
            
            <!-- Back Link -->
            <div class="article-back">
              <router-link to="/" class="back-link">← Back to Home</router-link>
            </div>
          </div>
          
          <!-- Right Sidebar -->
          <aside class="article-sidebar sidebar-right">
            <div class="ad-skyscraper">Advertisement block</div>
          </aside>
        </div>
      </div>
    </template>
    
    <div class="container" v-else style="padding: 4rem 2rem; text-align: center;">
      <h2>Article not found</h2>
      <router-link to="/" style="color: var(--purple);">Back to Home</router-link>
    </div>
  </main>
</template>

<style scoped>
.article-view { padding-bottom: 60px; }

.article-hero {
  position: relative; width: 100%; height: 400px;
  overflow: hidden; margin-bottom: 0;
}
.article-hero-img {
  width: 100%; height: 100%; object-fit: cover;
}
.article-hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to bottom, transparent 40%, var(--bg) 100%);
}

.article-body {
  max-width: 800px; margin: 0 auto; padding: 2rem 2rem 0;
  position: relative; margin-top: -60px;
}
.card-badge {
  display: inline-block; background: var(--purple); color: white;
  padding: 4px 12px; font-size: 12px; font-weight: 600; border-radius: 4px;
  text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px;
}
.article-title {
  font-size: 2.5rem; margin: 0 0 1.5rem; line-height: 1.2; font-weight: 800;
  letter-spacing: -1px;
}
.article-meta-bar {
  display: flex; align-items: center; gap: 1rem;
  color: var(--muted); margin-bottom: 2rem;
  padding-bottom: 2rem; border-bottom: 1px solid var(--border);
}
.meta-avatar { width: 48px; height: 48px; border-radius: 50%; }
.meta-details { font-size: 0.9rem; margin-top: 2px; }

.article-content {
  font-size: 1.1rem; line-height: 1.8; color: var(--text);
}
.article-content :deep(h2) {
  font-size: 1.6rem; font-weight: 800; margin: 2rem 0 1rem; letter-spacing: -0.5px;
}
.article-content :deep(h3) {
  font-size: 1.3rem; font-weight: 700; margin: 1.5rem 0 0.8rem;
}
.article-content :deep(p) { margin: 0 0 1.2rem; }
.article-content :deep(ul), .article-content :deep(ol) { margin: 0 0 1.2rem; padding-left: 1.5rem; }
.article-content :deep(li) { margin-bottom: 0.5rem; }
.article-content :deep(table) { width: 100%; border-collapse: collapse; margin: 1rem 0; }
.article-content :deep(th), .article-content :deep(td) {
  border: 1px solid var(--border); padding: 10px 14px; text-align: left; font-size: 0.95rem;
}
.article-content :deep(th) { background: var(--surface); font-weight: 700; }
.article-content :deep(em) { font-style: italic; }
.article-content :deep(strong) { font-weight: 700; }

.article-back { margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border); }
.back-link { color: var(--purple); font-weight: 600; font-size: 16px; }
.back-link:hover { text-decoration: underline; }

/* Grid of side advertisements */
.article-layout-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 2rem;
}
.article-sidebar {
  display: none; /* Hidden on mobile by default */
}
.ad-skyscraper {
  width: 100%;
  height: 600px;
  background: var(--surface);
  border: 1px dashed var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--muted);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: sticky;
  top: 100px;
}

@media (min-width: 1024px) {
  .article-body { max-width: 1200px; } /* Increase width to accommodate sidebars */
  .article-layout-grid {
    grid-template-columns: 200px 1fr 200px; /* Main layout with fixed sidebars */
  }
  .article-sidebar {
    display: block;
  }
  .article-main-content {
    max-width: 800px;
    margin: 0 auto;
    width: 100%;
  }
}

@media (max-width: 768px) {
  .article-hero { height: 260px; }
  .article-title { font-size: 1.8rem; }
}
</style>
