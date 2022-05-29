<script lang="ts" setup>
import {ProductType} from "~/types/product.tyoe";

const props = defineProps({
  product: {
    type: Object as PropType<ProductType>
  }
})


const currentCount = ref('1')
const numbers = ref([
    '1',
    '2',
    '3',
    '4',
    '5'
])
const productChecked = ref(false)

</script>
<template>
  <div class="cart-product">
    <v-row>
      <v-col class="cart-product__left" cols="6">
        <v-col cols="1" class="cart-product__check">
          <v-checkbox
              v-model="productChecked"
              hide-details
              color="primary"
          />
        </v-col>
        <v-col cols="11" class="cart-product__main">
          <div class="cart-product__image">
            <img :src="props.product.image" :alt="props.title">
          </div>
          <div class="cart-product__info">
            <div class="cart-product__title">{{ props.product.title }}</div>
            <div>{{ props.product.description }}</div>
            <div class="cart-product__favorite text-blue-accent-4">В избранное</div>
          </div>
        </v-col>
      </v-col>
      <v-col cols="3">
        <div class="cart-product__price">
          {{ props.product.price }}
        </div>
      </v-col>
      <v-col cols="3">
        <div class="cart-product__count">
          <v-select
              v-model="currentCount"
              :items="numbers"
              menu-props="auto"
              hide-details
              label="Select"
              single-line
          ></v-select>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<style scoped lang="scss">
.cart-product {
  &__left {
    display: flex;
    align-items: center;
  }

  &__info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

   &__image {
     width: 100px;
     height: 100px;
     margin-right: 1rem;

     img {
       width: 100%;
       height: 100%;
       object-fit: cover;
     }
   }

  &__check {
    justify-content: center;
  }

  &__main {
    display: flex;
  }
}
</style>
