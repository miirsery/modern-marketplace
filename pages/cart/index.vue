<script lang="ts" setup>
import {useCartStore} from "~/store/cart";

const cartStore = useCartStore()
const cartProducts = computed(() => (cartStore.getAllProductsInCart))

</script>
<template>
  <div>
    Cart
    <el-row>
      <el-col :span="20" v-if="cartStore.isLoaded">
        <cart-product
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
