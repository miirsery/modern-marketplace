<script lang="ts" setup>
const checkAll = ref(false)
const valid = ref(false)

const products = ref([
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
    id: 2,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 3,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 4,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
  {
    id: 5,
    image: 'https://cdn1.ozone.ru/s3/multimedia-o/wc100/6079536984.jpg',
    title: 'Ремень Fuzhiniao',
    description: 'цвет коричневый, размер 120, 170гр',
    price: 579,
    loyalty: 868,
    count: 3,
  },
])
const filteredProducts = ref(products)
let items = ref([])


const saveCheckedProducts = (value): void => {
  items.value.push(value)
}

const handleDeleteAllProducts = (): void => {
  if (checkAll.value === true) products.value = []

  filteredProducts.value = []

  for (const item of items.value) {
    const fp = products.value.filter(product => product.id !== item.id)

    for (const i of fp) {
      filteredProducts.value.push(i)
    }
  }

  /*filteredProducts.value = products.value.filter(product => {
    for (const item of items.value) {
      if (item.id !== product.id) {
        return product
      }
    }
  })*/
}

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
          <v-btn
              color="error"
              plain
              @click="handleDeleteAllProducts"
          >
            Delete checked
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <cart-product
              v-for="product in filteredProducts"
              :key="product.title"
              :product="product"
              :checkAll="checkAll"
              @check="saveCheckedProducts"
          />
        </v-col>
        <v-col cols="4">
          <nuxt-link to="/order">
            Перейти к оформлению
          </nuxt-link>
          <div class="cart__content">
            Cart on 513 р
          </div>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>
