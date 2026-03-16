import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ArticleView from '../views/ArticleView.vue';
import PrivacyView from '../views/PrivacyView.vue';
import TermsView from '../views/TermsView.vue';
import CookiesView from '../views/CookiesView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import ContactView from '../views/ContactView.vue';
import CategoriesView from '../views/CategoriesView.vue';
import AboutView from '../views/AboutView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/articulo/:id', name: 'article', component: ArticleView },
    { path: '/categorias', name: 'categories', component: CategoriesView },
    { path: '/contacto', name: 'contact', component: ContactView },
    { path: '/sobre', name: 'about', component: AboutView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/registro', name: 'register', component: RegisterView },
    { path: '/privacidad', name: 'privacy', component: PrivacyView },
    { path: '/terminos', name: 'terms', component: TermsView },
    { path: '/cookies', name: 'cookies', component: CookiesView },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    return { top: 0 };
  }
});

export default router;
