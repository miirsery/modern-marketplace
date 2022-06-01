<script lang="ts" setup>
import {useCartStore} from "~/store/cart";

const props = defineProps(['title'])
const store = useCartStore()
const mockData = [
  {
    id: 1,
    title: 'Нужные вещи | Кинг Стивен',
    image: 'https://cdn1.ozone.ru/s3/multimedia-x/wc1200/6009443841.jpg',
    price: 599
  }
]

const rating = ref(4)

const handleAddToCart = async (): Promise<void> => {
  // const data = await store.addToCart(mockData)
  store.books.push({
    id: 1,
    title: 'Нужные вещи | Кинг Стивен',
    image: 'https://cdn1.ozone.ru/s3/multimedia-x/wc1200/6009443841.jpg',
    price: 599
  })
}

</script>

<template>
  <div class="product mb-10">
    <div class="product__wrapper">
      <div class="product__image">
        <nuxt-link :to="`/product/${props.title}`">
          <img src="https://cdn1.ozone.ru/s3/multimedia-x/wc1200/6009443841.jpg" alt="Нужные вещи | Кинг Стивен" />
        </nuxt-link>
      </div>
      <div class="product__price">
        599 Р
      </div>
      <div class="product__title">
        'Нужные вещи | Кинг Стивен'
      </div>
      <v-rating
          class="product__rating"
          v-model="rating"
          background-color="indigo lighten-3"
          color="indigo"
      />
      <v-btn
          class="product__add"
          depressed
          color="primary"
          @click="handleAddToCart"
      >
        Add to cart
      </v-btn>
    </div>
  </div>
</template>

<style scoped lang="scss">
.product {
  &__wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  &__image {
    width: 230px;
    height: 260px;

    img {
      height: 100%;
      object-fit: cover;
    }
  }

  &__add {
    max-width: 60%;
  }

  &__rating {
    pointer-events: none;
  }
}
</style>
