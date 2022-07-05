<script lang="ts" setup>

import {useCategoryProducts} from "~/store/category-products";

const category = useRoute()
const categoryProductsStore = useCategoryProducts()
const products = ref<any>([])

const getCategoryProducts = async () => {
  await categoryProductsStore.getCategoryProducts(category.params.category)
  products.value = categoryProductsStore.getAllCategoryProducts
}
onMounted(() => {
  getCategoryProducts()
})

</script>
<template>
  <div class="category">
    <h2 class="text-title">
      {{ $route.params.category }}
    </h2>
    <el-row>
      <el-col :span="4">
        <category-filter />
      </el-col>
      <el-col :span="20">
        <el-row v-if="categoryProductsStore.isLoaded">
          <category-product
            v-for="product in products"
            :key="products.title"
            :product="product"
          />
      </el-row>
      </el-col>
    </el-row>
  </div>
</template>
