<script setup lang="ts">
import {useCatalogStore} from "~/store/catalog";
const store = useCatalogStore()
let categories = ref([])
const getCategories = async () => {
  categories.value = await store.getCatalog()
}
onMounted(() => {
  getCategories()
})
</script>

<template>
  <div class="category-dropdown d-flex position-absolute">
    <ul class="category-dropdown__categories">
            <!--This is getting data from backend.-->
<!--      <li class="main-aside__item" v-for="category in categories" :key="category.title">-->
<!--        <nuxt-link :to="{ path: `/category/${category.title}` }">{{ category.title }}</nuxt-link>-->
<!--      </li>-->
      <li>
        <nuxt-link class="category-dropdown__item" to='/category'>
          Electronic
        </nuxt-link>
      </li>
      <li>
        <nuxt-link class="category-dropdown__item" to='/category'>
          Electronic
        </nuxt-link>
      </li>
      <li>
        <nuxt-link class="category-dropdown__item" to='/category'>
          Electronic
        </nuxt-link>
      </li>
      <li>
        <nuxt-link class="category-dropdown__item" to='/category'>
          Electronic
        </nuxt-link>
      </li>
    </ul>
    <div class="category-dropdown__subcategories">
    </div>
  </div>
</template>

<style scoped lang="scss">
.category-dropdown {
  background-color: #fff;

  &__item {
    display: block;
    margin-bottom: 10px;
  }
}
</style>