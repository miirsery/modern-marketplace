<script lang="ts" setup>
import {categoriesApi} from "~/api/Categories.api";

const category = useRoute()
const products = ref([])

const getCategoryProducts = async () => {
  const [error, data] = await categoriesApi.getCategoryProducts(category.params.category)
  products.value = data
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
        <el-row>
          <lazy-category-product
            v-for="product in products"
            :key="products.title"
            :product="product"
          />
      </el-row>
      </el-col>
    </el-row>
  </div>
</template>
