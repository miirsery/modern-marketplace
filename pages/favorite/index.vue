<script lang="ts" setup>
import {useFavoriteStore} from "~/store/favorite";

const favoriteStore = useFavoriteStore()
const items = ref<any>([])

const getAllProducts = async (): Promise<void> => {
  items.value =  await favoriteStore.getProductsInFavorite()
}

onMounted(async () => {
  await getAllProducts()
})
</script>
<template>

</template>
