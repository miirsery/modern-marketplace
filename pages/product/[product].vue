<script lang="ts" setup>
import Cookies from "js-cookie";

const token = Cookies.get('token')
const runtimeConfig = useRuntimeConfig()
const route = useRoute()
const getAllProduct = async () => {
  // const data = cartStore.getAllProducts()
  // console.log(data)
  await fetch(`${runtimeConfig.public.BASE_URL}/api/product/v1/product-info/${route.params.product}/`, {
    method: 'get',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
      .then(r => r.json())
}

onMounted(() => {
  getAllProduct()
})
</script>
<template>
  {{ $route.params }}
</template>
