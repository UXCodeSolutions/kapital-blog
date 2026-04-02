<script setup>
defineProps({
  categories: {
    type: Array,
    required: true,
  },
  modelValue: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(['update:modelValue']);

const set = (cat) => emit('update:modelValue', cat);
</script>

<template>
  <div class="filters" aria-label="Filtros">
    <button
      v-for="c in categories"
      :key="c"
      class="chip"
      :class="{ 'is-active': modelValue === c }"
      type="button"
      @click="set(c)"
    >
      {{ c }}
    </button>
  </div>
</template>
