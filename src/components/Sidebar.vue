<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps({
  filteredArticles: { type: Array, required: true },
});

const emit = defineEmits(['search']);
const router = useRouter();
const searchQuery = ref('');

const handleSearch = () => {
  const q = searchQuery.value.trim();
  if (q) {
    emit('search', q);
    searchQuery.value = '';
  }
};

const goToTag = (tag) => {
  router.push({ path: '/categorias', query: { q: tag } });
};
</script>

<template>
  <aside class="sidebar" aria-label="Barra lateral">
    <div class="search-sidebar">
      <span class="search-icon">🔍</span>
      <form @submit.prevent="handleSearch" style="flex:1; display:flex;">
        <input v-model="searchQuery" type="text" placeholder="Search for articles, authors, or topics..." class="search-input" />
      </form>
      <div class="search-kbd">⌘K</div>
    </div>
    
    <div class="trending-tags">
      <span class="trending-label">Trending:</span>
      <a href="#" class="tag" @click.prevent="goToTag('Presupuesto')">#Presupuesto</a>
      <a href="#" class="tag" @click.prevent="goToTag('Inversión')">#Inversión</a>
      <a href="#" class="tag" @click.prevent="goToTag('Ahorro')">#Ahorro</a>
      <a href="#" class="tag" @click.prevent="goToTag('Crédito')">#Crédito</a>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-width: 700px;
  margin: 0 auto;
}

.search-sidebar {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 20px;
}

.search-icon {
  font-size: 16px;
  opacity: 0.6;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  color: var(--text);
}

.search-input::placeholder {
  color: var(--muted);
}

.search-kbd {
  background: var(--border);
  color: var(--muted);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  font-family: monospace;
}

.trending-tags {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.trending-label {
  font-weight: 600;
  font-size: 14px;
  color: var(--muted);
}

.tag {
  display: inline-block;
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.2s;
  text-decoration: none;
}

.tag:hover {
  border-color: var(--purple);
  color: var(--purple);
  background: transparent;
}
</style>
