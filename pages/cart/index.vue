<script lang="ts" setup>
const checkAll = ref(false)
const valid = ref(false)

const products = [
  {
    id: 1,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 1,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 1,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 1,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 1,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
]

</script>

<template>
  <div class="cart">
    <v-form v-model="valid">
      <v-row>
        <v-col>
          <h2 class="cart__title">Корзина <sup>17</sup></h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex align-center" cols="3">
          <v-checkbox
              hide-details
              v-model="checkAll"
              label="Check all"
              color="primary"
              class="mr-4"
          />
          <div class="red--text">Delete checked</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <cart-product
              v-for="product in products"
              :key="product.title"
              :product="product"
          />
        </v-col>
        <v-col cols="4">
          Перейти к оформлению
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>
