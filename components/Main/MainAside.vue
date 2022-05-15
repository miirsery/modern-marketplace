<script setup lang="ts">
import {useCatalogStore} from "~/store/catalog";

const store = useCatalogStore()

let categories = ref([])

const getCategories = async () => {
  categories.value = await store.getCatalog()
}
getCategories()

</script>

<template>
  <aside class="main-aside">
    <nav class="main-aside__navigation">
      <ul class="main-aside__menu">
        <li class="main-aside__item" v-for="category in categories" :key="category.title">
          <nuxt-link :to="{ path: `/category/${category.title}` }">{{ category.title }}</nuxt-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>
<style scoped lang="scss">
.main-aside {
  &__menu {}
}
</style>