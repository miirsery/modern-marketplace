<script lang="ts" setup>
import {useCartStore} from "~/store/cart";

const cartStore = useCartStore()
const cartProducts = ref([])

const getAllProduct = async () => {
  const [error, data] = await cartStore.getAllProducts()
  cartProducts.value = data[0].products
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
