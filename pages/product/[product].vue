<script lang="ts" setup>
import Cookies from "js-cookie";
import {useCartStore} from "~/store/cart";
import {ElMessage} from "element-plus";
import {productApi} from "~/api/Product.api";

const token = Cookies.get('token')
const route = useRoute()
const product = ref()
const cartStore = useCartStore()

const getProduct = async () => {
  const data = productApi.getProduct(route.params.product)
  console.log(data)
}

const handleAddToCart = async () => {
  const [error, data] = await cartStore.addToCart({
    product_id: '1',
    count_product: '1'
  })

  if (data.error) {
    ElMessage.error(data.error)
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
