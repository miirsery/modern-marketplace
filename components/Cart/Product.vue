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
const finedItemInCart = computed(() => (
    cartStore.getProduct(props.product['product_name'].id)
))

const countProducts = ref(finedItemInCart.value.count_product)
const handleUpdateProductCount = async (): Promise<void> => {
  if (finedItemInCart !== undefined) {
    const [_, data] = await cartStore.addToCart({
      product_id: finedItemInCart.value.id,
      new_count_products: countProducts.value
    }, 'patch')

    await cartStore.updateCountProductsInCart(data.count_products_in_basket)
  }
}

</script>
<template>
  <el-row class="cart-product">
    <el-col :span="2">
      <div class="cart-product__image">
        <img :src="product['product_name'].photo[0].image" alt="image">
      </div>
    </el-col>
    <el-col :span="16">
      <div class="cart-product__title">
        {{ product['product_name'].title }}
      </div>
      <el-button class="cart-product__button">
        В избранное
      </el-button> |
      <el-button class="cart-product__button">
        Удалить
      </el-button>
    </el-col>
    <el-col :span="4">
      <p>
        {{ product['final_price'] }} Р
      </p>
      <p>
        {{ product['final_price_not_discount'] }}
        <span>Скидка {{ product['final_total_discount'] }}</span>
      </p>
    </el-col>
    <el-col :span="2">
      <el-input-number
          v-model="countProducts"
          :min="1"
          :max="10"
          @change="handleUpdateProductCount"
      />
    </el-col>
  </el-row>
</template>

<style scoped lang="scss">
.cart-product {
  margin-bottom: 24px;

  &__image {
    width: 100px;
    height: 100px;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}
</style>
