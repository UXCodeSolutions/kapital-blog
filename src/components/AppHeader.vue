<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps({
  items: { type: Array, required: true },
  theme: { type: String, required: true },
});

const emit = defineEmits(['toggle-theme']);
const router = useRouter();

const open = ref(false);
const searchQuery = ref('');

const toggle = () => { open.value = !open.value; };

const toggleTheme = () => { emit('toggle-theme'); };

const isLoggedIn = computed(() => !!localStorage.getItem('kapital-token'));
const currentUser = computed(() => {
  const u = localStorage.getItem('kapital-user');
  return u ? JSON.parse(u) : null;
});

const logout = () => {
  localStorage.removeItem('kapital-token');
  localStorage.removeItem('kapital-user');
  router.push('/');
};

const handleSearch = () => {
  const q = searchQuery.value.trim();
  if (q) {
    router.push({ path: '/categorias', query: { q } });
    searchQuery.value = '';
    showDropdown.value = false;
    open.value = false;
  }
};

const searchResults = ref([]);
const isSearching = ref(false);
const showDropdown = ref(false);
let debounceTimer = null;

const onSearchInput = () => {
  const q = searchQuery.value.trim();
  if (!q) {
    showDropdown.value = false;
    searchResults.value = [];
    return;
  }

  showDropdown.value = true;
  isSearching.value = true;

  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(async () => {
    try {
      const res = await fetch(`http://localhost:8000/articles?limit=5&q=${encodeURIComponent(q)}`);
      if (res.ok) {
        searchResults.value = await res.json();
      }
    } catch (err) {
      console.error('Error in live search:', err);
    } finally {
      isSearching.value = false;
    }
  }, 300);
};

const closeSearchDropdown = (e) => {
  const isClickInside = e.target.closest('.header-search');
  if (!isClickInside) {
    showDropdown.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', closeSearchDropdown);
});
</script>

<template>
  <header class="header" role="banner">
    <a class="skip-link" href="#contenido">Saltar al contenido</a>

    <div class="container header-inner">
      <router-link to="/" class="brand" aria-label="Marca" style="text-decoration:none">
        <div class="logo-img">
          <svg viewBox="0 0 24 24" fill="none" class="logo-svg" xmlns="http://www.w3.org/2000/svg"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="#7C3AED"/><path d="M8 7V17M8 12H11.5M16 7L11.5 12M11.5 12L16 17" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="brand-text">
          <span class="brand-name">Kapital Blog</span>
        </div>
      </router-link>

      <nav class="nav" aria-label="Navegación principal">
        <router-link v-for="it in items" :key="it.path" :to="it.path" active-class="active" :exact="it.path === '/'">{{ it.label }}</router-link>
      </nav>
      
      <div class="header-search">
        <span class="search-icon">🔍</span>
        <form @submit.prevent="handleSearch">
          <input 
            v-model="searchQuery" 
            @input="onSearchInput"
            @focus="onSearchInput"
            type="text" 
            placeholder="Search articles..." 
            class="search-input" 
          />
        </form>
        
        <!-- Live Search Dropdown -->
        <div v-if="showDropdown" class="search-dropdown">
          <div v-if="isSearching" class="search-msg">Buscando...</div>
          <div v-else-if="searchResults.length === 0" class="search-msg">No se encontraron artículos.</div>
          <template v-else>
            <router-link 
              v-for="res in searchResults" 
              :key="res.id" 
              :to="'/articulo/' + res.id" 
              class="search-result-item"
              @click="showDropdown = false; searchQuery = ''"
            >
              <div class="search-result-img" :style="{ backgroundImage: 'url(' + (res.image_url || 'https://images.unsplash.com/photo-1540420773420-3366772f4999?q=80&w=100') + ')' }"></div>
              <div class="search-result-info">
                <span class="search-result-title">{{ res.title }}</span>
                <span class="search-result-cat">{{ res.category }}</span>
              </div>
            </router-link>
          </template>
        </div>
      </div>

      <div class="header-actions">
         <template v-if="isLoggedIn">
           <span class="user-greeting">👋 {{ currentUser?.username }}</span>
           <button @click="logout" class="login-link" style="background:none;border:none;cursor:pointer;color:inherit;font-size:14px;">Logout</button>
         </template>
         <template v-else>
           <router-link to="/login" class="login-link">Log In</router-link>
           <router-link to="/registro" class="btn-subscribe">Subscribe</router-link>
         </template>
         <button
          class="theme-toggle"
          type="button"
          aria-label="Cambiar tema"
          :aria-pressed="theme === 'dark' ? 'true' : 'false'"
          @click="toggleTheme"
        >
          <span class="theme-toggle-icon" aria-hidden="true">{{ theme === 'dark' ? '☀' : '☾' }}</span>
        </button>
      </div>

      <button
        class="nav-toggle"
        type="button"
        :aria-expanded="open ? 'true' : 'false'"
        aria-controls="nav-mobile"
        @click="toggle"
      >
        <span class="nav-toggle-line" aria-hidden="true"></span>
        <span class="nav-toggle-line" aria-hidden="true"></span>
        <span class="nav-toggle-line" aria-hidden="true"></span>
        <span class="sr-only">Abrir menú</span>
      </button>
    </div>

    <div class="container nav-mobile" id="nav-mobile" v-show="open" aria-label="Menú móvil">
      <router-link v-for="it in items" :key="'m-'+it.path" :to="it.path" @click="open = false">{{ it.label }}</router-link>
       <div class="mobile-actions">
         <template v-if="isLoggedIn">
           <span>👋 {{ currentUser?.username }}</span>
           <button @click="logout; open = false" class="login-link" style="background:none;border:none;cursor:pointer;">Logout</button>
         </template>
         <template v-else>
           <router-link to="/login" @click="open = false" class="login-link">Log In</router-link>
           <router-link to="/registro" @click="open = false" class="btn-subscribe">Subscribe</router-link>
         </template>
       </div>
    </div>
  </header>
</template>

<style scoped>
.user-greeting { font-size: 14px; font-weight: 500; }

.header-search {
  position: relative;
}

.search-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  background: var(--surface);
  border-radius: 12px;
  box-shadow: var(--shadow);
  z-index: 1000;
  max-height: 400px;
  overflow-y: auto;
  border: 1px solid var(--border);
}

.search-msg {
  padding: 16px;
  text-align: center;
  color: var(--muted);
  font-size: 14px;
}

.search-result-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  text-decoration: none;
  color: var(--text);
  border-bottom: 1px solid var(--border);
  transition: background 0.2s;
}

.search-result-item:last-child {
  border-bottom: none;
}

.search-result-item:hover {
  background: var(--bg-offset);
}

.search-result-img {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background-size: cover;
  background-position: center;
  flex-shrink: 0;
}

.search-result-info {
  display: flex;
  flex-direction: column;
}

.search-result-title {
  font-size: 14px;
  font-weight: 600;
  margin: 0;
  line-height: 1.3;
}

.search-result-cat {
  font-size: 12px;
  color: var(--primary);
  margin-top: 4px;
}
</style>
