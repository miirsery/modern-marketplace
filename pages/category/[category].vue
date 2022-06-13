<script lang="ts" setup>
import {categoriesApi} from "~/api/Categories.api";
import {useUserStore} from "~/store/user";

const category = useRoute()
const products = ref([])

const runtimeConfig = useRuntimeConfig()

// const userStore = useUserStore()

const getCategoryProducts = async () => {
  // const [error, data] = await categoriesApi.getCategoryProducts(category.params.category)
  // console.log(data)
  fetch(`${runtimeConfig.public.BASE_URL}/api/product/catalog/${category.params.category}/`, {
    method: 'get',
  })
      .then(r => r.json())
      .then(r => {
        products.value = r
      })
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
          <el-col :span="3">
            <lazy-category-product
              v-for="product in products"
              :key="products.title"
              :product="product"
            />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>
