<script lang="ts">

</script>
<template>
  <div class="category">
    {{ $route.params.category }}
    <div class="d-flex">
      <category-filters />
      <div class="category__products d-flex flex-wrap">
        <category-product v-for="(item, index) in 10" :key="index" title="thing"/>
      </div>
    </div>
  </div>
</template>