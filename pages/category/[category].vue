<script lang="ts">

</script>
<template>
  <div class="category d-fled">
    <category-filters />
    <category-product :id="$route.params.category" />
  </div>
</template>