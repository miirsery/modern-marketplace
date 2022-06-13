<script lang="ts" setup>
import Cookies from "js-cookie";
import {useCartStore} from "~/store/cart";
import {ElMessage} from "element-plus";

const token = Cookies.get('token')
const runtimeConfig = useRuntimeConfig()
const route = useRoute()
const product = ref()
// const cartStore = useCartStore()

const getProduct = async () => {
  // const data = cartStore.getAllProducts()
  // console.log(data)
  await fetch(`${runtimeConfig.public.BASE_URL}/api/product/v1/product-info/${route.params.product}/`, {
    method: 'get',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
      .then(r => r.json())
      .then(r => {
        product.value = r
      })
}

const handleAddToCart = async () => {
  try {
    await fetch(`${runtimeConfig.public.BASE_URL}/api/cart/add/`, {
      method: 'post',
      body: JSON.stringify({
        product_id: product.value?.id,
        count_product: '1',
      }),
      headers: {
        'Content-type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    }).then(r => r.json()).then(r => {
      if (r.error) {
        ElMessage.error(r.error)
      }
    })
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  getProduct()
})
</script>
<template>
  <div class="product">
    <el-row>
      <el-col :span="4">
        <div class="product__image">
          <img :src="product?.photo[0].image" :alt="product?.title">
        </div>
      </el-col>
      <el-col :span="12">
        <p>{{ product?.description }}</p>
      </el-col>
    </el-row>
    <el-col :span="8">
      <el-button type="primary" @click="handleAddToCart">Добавить в корзину</el-button>
    </el-col>
  </div>
</template>
