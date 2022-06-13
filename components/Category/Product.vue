<script lang="ts" setup>
import {useCartStore} from "~/store/cart";
import {ElMessage} from "element-plus";

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const cartStore = useCartStore()

const handleAddToCart = async () => {
  const [error, data] = await cartStore.addToCart({
    product_id: props.product.id,
    count_product: '1'
  })
  if (data.error) {
    ElMessage.error(data.error)
  }
}
</script>
<template>
  <div class="category-product">
    <nuxt-link :to="`/product/${product.id}`">
      <div class="category-product__images">
        <img :src="product.photo[0].image" :alt="product.title">
      </div>
    </nuxt-link>
    <div class="category-product__price">
      <span>{{ product.price_now }} | {{ product.price_old }}</span>
    </div>
    <h3 class="category-product__tittle">{{ product.title }}</h3>
    <el-button type="primary" @click="handleAddToCart">Добавить в корзину</el-button>
  </div>
</template>
