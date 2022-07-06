<script lang="ts" setup>
import {ElMessage} from "element-plus";
import {useFavoriteStore} from "~/store/favorite";
import {useCartStore} from "~/store/cart";

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const cartStore = useCartStore()
const favoriteStore = useFavoriteStore()

const countProducts = ref(0)
const finedItemIdInCart = ref(null)

watch(
    () => cartStore.getAllProductsInCart,
    (newVal, _) => {
      if (newVal !== undefined) {
        const { product_name, count_product, id } = newVal.find((item) => item.product_name.id === props.product.id)
        const finedItemId = product_name.id
        const finedItemCount = count_product
        finedItemIdInCart.value = id

        countProducts.value = finedItemId !== undefined ? finedItemCount : 0
      }
    }
)


const openSuccessMessage = (): void => {
  ElMessage({
    message: 'Товар успешно добавлен в корзину',
    type: 'success'
  })
}

const handleAddToCart = async (): Promise<void> => {
  if (countProducts.value === 0) {
    countProducts.value++
  }

  const [_, data] = await cartStore.addToCart({
    product_id: props.product.id,
    count_product: countProducts.value
  }, 'post')

  if (data.error) {
    ElMessage.error(data.error)
  } else {
    openSuccessMessage()
    await cartStore.updateCountProductsInCart(data.count_products_in_basket)
  }
}

const handleUpdateProductCount = async (): Promise<void> => {
  const [_, data] = await cartStore.addToCart({
    product_id: finedItemIdInCart.value,
    new_count_products: countProducts.value
  }, 'patch')

  await cartStore.updateCountProductsInCart(data.count_products_in_basket)
}

const handleAddToFavorite = async (): Promise<void> => {
  await favoriteStore.addToFavorite({
    product_id: props.product.id
  })
  await favoriteStore.getProductsInFavorite()
}

onMounted(async () => {
  if (await cartStore.getAllProductsInCart !== undefined && cartStore.getAllProductsInCart.lenght > 0) {
    console.log(cartStore.getAllProductsInCart)
    countProducts.value = cartStore.getAllProductsInCart.find((item) => item.product_name.id === props.product.id).count_product
  }
})

</script>
<template>
  <el-col :span="6" class="category-product">
    <nuxt-link :to="`/product/${product.id}`" class="category-product__image">
      <div class="category-product__switch image-switch">
        <div class="image-switch__item" v-for="image in product.photo">
          <div class="image-switch__img">
            <img :src="image.image" alt="Мак" />
          </div>
        </div>
      </div>
      <ul class="category-product__image-pagination image-pagination" aria-hidden="true">
        <li class="image-pagination__item"></li>
      </ul>
    </nuxt-link>
    <p class="category-product__price">
      {{ product.price_now }} ₽
      <span v-if="product.price_old">{{ product.price_old }} ₽</span>
    </p>
    <p class="mb-12">{{ product.title }}</p>
    <el-row justify="space-between">
      <el-button
          v-if="countProducts === 0"
          size="small"
          type="primary"
          @click="handleAddToCart"
      >
        Добавить в корзину
      </el-button>
      <el-input-number
          v-else
          v-model="countProducts"
          :min="1"
          :max="10"
          @change="handleUpdateProductCount"
      />
      <el-button class="category-product__favorite-button" @click="handleAddToFavorite">
        <common-icon
            svg="favorite-icon"
            :class="[{
                'category-product__favorite-icon--in-cart': favoriteStore.hasFavoriteProduct(product.id)
               },
              'category-product__favorite-icon'
             ]"
        />
      </el-button>
    </el-row>
  </el-col>
</template>

<style scoped lang="scss">
.category-product {
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  padding: 9px 20px 20px;
  font-size: 14px;
  background-color: #fff;
  margin-right: 12px;

  &__image {
    position: relative;
    overflow: hidden;
    display: block;
    height: 180px;
  }

  &__favorite {
    &-icon {
      width: 24px;
      height: 24px;

      &--in-cart {
        color: $color-danger;
      }
    }
  }

  &__price {
    margin: 8px 0;
    font-size: 18px;
    font-weight: 600;
    line-height: 1.2;

    span {
      position: relative;
      font-size: 12px;
      line-height: 1.1;
      color: $color-medium-gray;

      &::after {
        content: '';
        left: 0;
        right: 0;
        top: 50%;
        position: absolute;
        width: 100%;
        height: 1px;
        background-color: $color-light-red;
        transform: rotate(-7deg);
      }
    }
  }
}


.image-switch {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 20;
  width: 100%;
  height: 100%;
  display: flex;

  &__item {
    flex-grow: 1;
    cursor: pointer;

    &:first-child,
    &:hover {
      .image-switch__img {
        opacity: 1;
        z-index: -1;
      }
    }
  }

  &__img {
    position: absolute;
    left: 50%;
    top: 0;
    z-index: 2;
    width: 100%;
    height: 100%;
    transform: translateX(-50%);
    pointer-events: none;
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;

    img {
      display: block;
      max-width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}

.image-pagination {
  position: absolute;
  z-index: 30;
  left: 0;
  bottom: 15px;
  width: 100%;
  display: flex;
  justify-content: center;

  &__item {
    display: block;
    width: 4px;
    height: 4px;
    border-radius: 100%;
    margin: 0 3px;
    background-color: #c4c4c4;

    &--active {
      background-color: $color-accent;
    }
  }
}



</style>
