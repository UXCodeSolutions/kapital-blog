<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Sidebar from '../components/Sidebar.vue';
import SliderHeader from '../components/SliderHeader.vue';
import AdPlaceholder from '../components/AdPlaceholder.vue';
import ArticleCard from '../components/ArticleCard.vue';

const router = useRouter();
const articles = ref([]);
const isLoading = ref(true);
const skip = ref(0);
const limit = 6;
const hasMore = ref(true);
const newsletterEmail = ref('');
const newsletterStatus = ref('');
const newsletterLoading = ref(false);

const API = 'http://localhost:8000';

const imgKeys = ['typography', 'remote', 'smarthome', 'travel', 'mindfulness', 'web3'];

const enrichArticles = (data, startIndex = 0) => {
  return data.map((item, index) => {
    const i = startIndex + index;
    return {
      ...item,
      imgKey: imgKeys[i % imgKeys.length],
    };
  });
};

const fetchArticles = async () => {
  try {
    const response = await fetch(`${API}/articles?skip=0&limit=${limit}`);
    if (!response.ok) throw new Error('Error al cargar artículos');
    const data = await response.json();
    articles.value = enrichArticles(data);
    skip.value = data.length;
    hasMore.value = data.length >= limit;
  } catch (error) {
    console.error('Error:', error);
  } finally {
    isLoading.value = false;
  }
};

const loadMore = async () => {
  try {
    const response = await fetch(`${API}/articles?skip=${skip.value}&limit=${limit}`);
    if (!response.ok) throw new Error('Error');
    const data = await response.json();
    if (data.length === 0) {
      hasMore.value = false;
      return;
    }
    articles.value = [...articles.value, ...enrichArticles(data, skip.value)];
    skip.value += data.length;
    hasMore.value = data.length >= limit;
  } catch (error) {
    console.error('Error:', error);
  }
};

const subscribeNewsletter = async () => {
  if (!newsletterEmail.value) return;
  newsletterLoading.value = true;
  newsletterStatus.value = '';
  try {
    const res = await fetch(`${API}/newsletter/subscribe`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: newsletterEmail.value })
    });
    const data = await res.json();
    newsletterStatus.value = data.message;
    if (data.status === 'subscribed') newsletterEmail.value = '';
  } catch (e) {
    newsletterStatus.value = 'Error al suscribir. Intenta de nuevo.';
  } finally {
    newsletterLoading.value = false;
  }
};

const handleSearch = (query) => {
  if (query.trim()) {
    router.push({ path: '/categorias', query: { q: query.trim() } });
  }
};

const goToCategory = (cat) => {
  router.push({ path: '/categorias', query: { cat } });
};

const goToSearch = (tag) => {
  router.push({ path: '/categorias', query: { q: tag } });
};

onMounted(() => {
  fetchArticles();
});

const browseCategories = [
  { label: 'Presupuesto', count: 'Artículos', imgKey: 'cat-design' },
  { label: 'Ahorro', count: 'Artículos', imgKey: 'cat-technology' },
  { label: 'Inversión', count: 'Artículos', imgKey: 'cat-business' },
  { label: 'Crédito', count: 'Artículos', imgKey: 'cat-lifestyle' },
];

const authors = [
  { name: 'Elena Vance', img: 'https://i.pravatar.cc/100?img=5' },
  { name: 'Julian Thorne', img: 'https://i.pravatar.cc/100?img=11' },
  { name: 'Sarah Chen', img: 'https://i.pravatar.cc/100?img=9' },
  { name: 'Marcus Miller', img: 'https://i.pravatar.cc/100?img=12' },
  { name: 'Aria Brooks', img: 'https://i.pravatar.cc/100?img=5' },
];

const scrollTo = (id) => {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
};
</script>

<template>
  <main id="contenido" class="site-main" role="main">
    
    <!-- HEADER SLIDER (Actuando como Hero Dinámico) -->
    <SliderHeader :articles="articles" v-if="articles.length > 0" />

    <!-- AD PLACEHOLDER TOP -->
    <AdPlaceholder text="Ad Space - Top Banner" height="90px" />

    <section class="section search-bar-section">
       <div class="container">
          <Sidebar :filteredArticles="articles" @search="handleSearch" />
       </div>
    </section>

    <section class="section" id="articulos" aria-label="Latest Insights">
      <div class="container layout">
        <div class="content full-width">
          <div class="section-head title-row">
            <div>
              <h2>Latest Insights</h2>
              <p class="subtitle">Explore our newest perspectives on markets, investing, and the global economy.</p>
            </div>
            <router-link to="/categorias" class="view-all">View All Articles &gt;</router-link>
          </div>

          <div class="cards architecture-grid" aria-label="Listado de artículos" v-if="!isLoading">
            <ArticleCard v-for="a in articles" :key="a.id" :article="a" />
          </div>
          <div v-else style="padding: 2rem; text-align: center; color: var(--muted);">
            Cargando artículos...
          </div>
          
          <div class="load-more-container" v-if="!isLoading && hasMore">
            <button class="btn btn-outline load-more" @click="loadMore">Load More Stories</button>
          </div>
        </div>
      </div>
    </section>
    
    <!-- AD PLACEHOLDER MIDDLE -->
    <AdPlaceholder text="Ad Space - In Feed" height="150px" />

    <section class="section" id="categorias" aria-label="Browse by Category">
      <div class="container">
         <div class="section-head title-row">
            <div>
              <h2>Browse by Category</h2>
              <p class="subtitle">Deep dives into the topics that matter most.</p>
            </div>
            <router-link to="/categorias" class="view-all">Explore All Topics &gt;</router-link>
          </div>
          
          <div class="browse-categories-grid">
            <div
              class="cat-card"
              v-for="cat in browseCategories"
              :key="cat.label"
              :data-img="cat.imgKey"
              @click="goToCategory(cat.label)"
              style="cursor: pointer;"
            >
              <div class="cat-content">
                <span class="cat-count">{{ cat.count }}</span>
                <h3 class="cat-title">{{ cat.label }}</h3>
              </div>
            </div>
          </div>
      </div>
    </section>
    
    <section class="section newsletter-section" aria-label="Newsletter">
      <div class="container">
        <div class="newsletter-banner">
           <div class="newsletter-icon" aria-hidden="true">
             <svg class="icon" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M4 6h16v12H4z" />
               <path d="m4 7 8 6 8-6" />
             </svg>
           </div>
           <h2>The Sunday Briefing</h2>
           <p>Join 50,000+ investors and financial professionals who receive our weekly curated insights on markets, wealth management, and macro trends. No spam, just substance.</p>
           <form class="newsletter-inline-form" @submit.prevent="subscribeNewsletter">
              <input v-model="newsletterEmail" type="email" placeholder="name@example.com" required />
              <button class="btn-subscribe-white" type="submit" :disabled="newsletterLoading">
                {{ newsletterLoading ? 'Sending...' : 'Subscribe' }}
              </button>
           </form>
           <p v-if="newsletterStatus" class="newsletter-meta" style="font-weight:600; opacity:1 !important;">{{ newsletterStatus }}</p>
           <p class="newsletter-meta">By subscribing you agree to our privacy policy. Unsubscribe anytime.</p>
        </div>
      </div>
    </section>
    
    <!-- Eliminated The Voices of Kapital section -->
  </main>
</template>
