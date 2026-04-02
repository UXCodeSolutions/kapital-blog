<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ArticleCard from '../components/ArticleCard.vue';

const route = useRoute();
const router = useRouter();

const articles = ref([]);
const categories = ref([]);
const selectedCategory = ref('');
const searchQuery = ref('');
const isLoading = ref(true);

const API = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '');

const imgKeys = ['typography', 'remote', 'smarthome', 'travel', 'mindfulness', 'web3'];
const authorsList = [
  { name: 'Julian Thorne', avatar: 'https://i.pravatar.cc/100?img=11' },
  { name: 'Sarah Chen', avatar: 'https://i.pravatar.cc/100?img=9' },
  { name: 'Marcus Miller', avatar: 'https://i.pravatar.cc/100?img=12' },
  { name: 'Lars Jensen', avatar: 'https://i.pravatar.cc/100?img=13' },
  { name: 'Aria Brooks', avatar: 'https://i.pravatar.cc/100?img=5' },
  { name: 'Kevin Wright', avatar: 'https://i.pravatar.cc/100?img=15' }
];

const enrichArticles = (data) => {
  return data.map((item, index) => ({
    ...item,
    imgKey: imgKeys[index % imgKeys.length],
    author: authorsList[index % authorsList.length].name,
    authorAvatar: authorsList[index % authorsList.length].avatar,
  }));
};

const fetchCategories = async () => {
  try {
    const res = await fetch(`${API}/categories`);
    if (res.ok) categories.value = await res.json();
  } catch (e) { console.error(e); }
};

const fetchArticles = async (cat, q) => {
  isLoading.value = true;
  try {
    const params = new URLSearchParams();
    if (cat) params.set('category', cat);
    if (q) params.set('q', q);
    const url = `${API}/articles${params.toString() ? '?' + params.toString() : ''}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Error');
    articles.value = enrichArticles(await res.json());
  } catch (e) { console.error(e); }
  finally { isLoading.value = false; }
};

const selectCategory = (cat) => {
  selectedCategory.value = cat;
  searchQuery.value = '';
  router.replace({ query: cat ? { cat } : {} });
  fetchArticles(cat, '');
};

onMounted(async () => {
  await fetchCategories();
  const catFromQuery = route.query.cat || '';
  const qFromQuery = route.query.q || '';
  selectedCategory.value = catFromQuery;
  searchQuery.value = qFromQuery;
  await fetchArticles(catFromQuery, qFromQuery);
});

watch(() => route.query, (newQuery) => {
  selectedCategory.value = newQuery.cat || '';
  searchQuery.value = newQuery.q || '';
  fetchArticles(newQuery.cat || '', newQuery.q || '');
});
</script>

<template>
  <main class="site-main categories-view">
    <div class="container">
      <div class="categories-header">
        <h1>{{ searchQuery ? 'Results: "' + searchQuery + '"' : 'Categories' }}</h1>
        <p class="subtitle">{{ searchQuery ? 'Showing articles matching your search' : 'Explore articles by topic' }}</p>
      </div>

      <div class="category-chips">
        <button
          class="chip" :class="{ 'is-active': !selectedCategory }"
          @click="selectCategory('')"
        >All</button>
        <button
          v-for="cat in categories" :key="cat.label"
          class="chip" :class="{ 'is-active': selectedCategory === cat.label }"
          @click="selectCategory(cat.label)"
        >{{ cat.label }} <span class="chip-count">({{ cat.count }})</span></button>
      </div>

      <div class="cards architecture-grid" v-if="!isLoading && articles.length > 0">
        <ArticleCard v-for="a in articles" :key="a.id" :article="a" />
      </div>
      <div v-else-if="!isLoading" class="empty-state">
        <p>No articles found in this category.</p>
      </div>
      <div v-else class="loading-state">
        Loading articles...
      </div>
    </div>
  </main>
</template>

<style scoped>
.categories-view { padding: 60px 0; }
.categories-header { margin-bottom: 32px; }
.categories-header h1 { font-size: 36px; font-weight: 800; margin: 0 0 8px; letter-spacing: -1px; }

.category-chips { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; }
.chip {
  border: 1px solid var(--border); background: var(--surface);
  padding: 8px 16px; border-radius: 99px; font-weight: 600; font-size: 14px;
  cursor: pointer; transition: all 0.2s; color: var(--text);
}
.chip:hover { border-color: var(--purple); }
.chip.is-active { background: var(--purple); color: white; border-color: var(--purple); }
.chip-count { opacity: 0.7; font-weight: 400; }

.empty-state, .loading-state { text-align: center; padding: 60px 0; color: var(--muted); font-size: 18px; }
</style>
