<script lang="ts" setup>
import {useFavoriteStore} from "~/store/favorite";

const favoriteStore = useFavoriteStore()
const items = ref<any>(favoriteStore.getAllProducts)

onMounted(async () => {
  await favoriteStore.getProductsInFavorite()
})
</script>
<template>
  <div class="favorite">
    <favorite-product
      v-for="product in items"
      :key="product.id"
      :product="product"
    />
  </div>
</template>
