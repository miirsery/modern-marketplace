<script lang="ts" setup>
import {useCartStore} from "~/store/cart";
import Cookies from "js-cookie";

const runtimeConfig = useRuntimeConfig()
// const cartStore = useCartStore()
const cartProducts = ref([])

const token = Cookies.get('token')

const getAllProduct = async () => {
  // const data = cartStore.getAllProducts()
  // console.log(data)
  await fetch(`${runtimeConfig.public.BASE_URL}/api/cart/list-products-cart/`, {
    method: 'get',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
      .then(r => r.json())
      .then(r => {
        cartProducts.value = r[0].products
      })
}
onMounted(() => {
  getAllProduct()
})
</script>
<template>
  <div>
    Cart
    <el-row>
      <el-col :span="20">
        <lazy-cart-product
            v-for="product in cartProducts"
            :key="product.id"
            :product="product"
        />
      </el-col>
      <el-col :span="4">
        <lazy-cart-actions />
      </el-col>
    </el-row>
  </div>
</template>
