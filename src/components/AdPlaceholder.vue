<script setup>
defineProps({
  text: {
    type: String,
    default: 'Advertisement'
  },
  height: {
    type: String,
    default: '90px'
  }
});
</script>

<template>
  <div class="ad-placeholder container" :style="{ minHeight: height }">
    <span class="ad-text">{{ text }}</span>
  </div>
</template>

<style scoped>
.ad-placeholder {
  background: var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  border-radius: 8px;
  margin: 2rem auto;
  padding: 1rem;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}
.ad-text {
  color: var(--muted);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}
</style>
