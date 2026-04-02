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
    { path: '/article/:id', name: 'article', component: ArticleView },
    { path: '/categories', name: 'categories', component: CategoriesView },
    { path: '/contact', name: 'contact', component: ContactView },
    { path: '/about', name: 'about', component: AboutView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: RegisterView },
    { path: '/privacy', name: 'privacy', component: PrivacyView },
    { path: '/terms', name: 'terms', component: TermsView },
    { path: '/cookies', name: 'cookies', component: CookiesView },
    // Redirects from old Spanish routes
    { path: '/articulo/:id', redirect: to => `/article/${to.params.id}` },
    { path: '/categorias', redirect: '/categories' },
    { path: '/contacto', redirect: '/contact' },
    { path: '/sobre', redirect: '/about' },
    { path: '/registro', redirect: '/register' },
    { path: '/privacidad', redirect: '/privacy' },
    { path: '/terminos', redirect: '/terms' },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    return { top: 0 };
  }
});

export default router;
