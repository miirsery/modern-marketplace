<script lang="ts" setup>
const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})
</script>
<template>
  {{ product }}
</template>
