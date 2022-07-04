<script lang="ts" setup>
import {categoriesApi} from "~/api/Categories.api";
import {useCartStore} from "~/store/cart";
const cartStore = useCartStore()
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
        <el-row v-if="cartStore.isLoaded">
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
