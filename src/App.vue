<script setup>
import { ref, onMounted, computed } from 'vue';
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';

const THEME_KEY = 'kapital-theme';

const getPreferredTheme = () => {
  const stored = localStorage.getItem(THEME_KEY);
  if (stored === 'light' || stored === 'dark') return stored;
  return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
};

const theme = ref(getPreferredTheme());

const applyTheme = (t) => {
  document.documentElement.setAttribute('data-theme', t);
};

applyTheme(theme.value);

const navItems = [
  { path: '/', label: 'Home' },
  { path: '/categorias', label: 'Categorías' },
  { path: '/sobre', label: 'Sobre' },
  { path: '/contacto', label: 'Contacto' },
];

const toggleTheme = () => {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
  localStorage.setItem(THEME_KEY, theme.value);
  applyTheme(theme.value);
};

const year = new Date().getFullYear();
</script>

<template>
  <AppHeader :items="navItems" :theme="theme" @toggle-theme="toggleTheme" />
  <router-view />
  <AppFooter :year="year" />
</template>
