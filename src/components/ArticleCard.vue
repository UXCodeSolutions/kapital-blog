<script setup>
defineProps({
  article: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <router-link :to="'/articulo/' + article.id" style="text-decoration: none; color: inherit; display: block;">
    <article class="card" :data-category="article.category.toLowerCase()">
      <div class="card-media">
        <div class="img" :data-img="article.imgKey" role="img" :aria-label="article.title"></div>
      </div>
      <div class="card-body">
        <div class="card-meta-top">
          <span class="badge">{{ article.category }}</span>
        </div>
        <h3 class="card-title">{{ article.title }}</h3>
        
        <div class="card-meta-bottom" style="margin-top: auto; padding-top: 1rem;">
          <div class="article-meta" style="color: var(--muted); font-size: 0.9rem;">
            <span class="meta-item">{{ article.date }}</span>
            <span class="meta-dot">·</span>
            <span class="meta-item">{{ article.readTime }}</span>
          </div>
        </div>
      </div>
    </article>
  </router-link>
</template>
