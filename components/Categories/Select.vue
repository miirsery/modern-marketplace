<script lang="ts" setup>
import { categoriesApi }  from '@/api/Categories.api'

const props = defineProps({
  isVisible: {
    type: Boolean,
    default: false
  }
})

const categories = ref([])

const emit = defineEmits([
    'closeCategories'
])

const handleCloseCategories = () => {
  console.log('emit')
  emit('closeCategories')
}

const getCategories = async () => {
  const [error, data] = await categoriesApi.getCategories()
  categories.value = data
}

watch(() => props.isVisible,
    (old, newValue) => {
      if (!newValue) {
        getCategories()
      }
    }
)

</script>

<template>
  <div class="categories-select">
    <ClientOnly>
      <el-drawer
          v-model="isVisible"
          title="All categories"
          direction="ttb"
          modal-class="categories-select__categories"
          @close="handleCloseCategories"
      >
        <el-row>
          <el-col :span="6">
            <div v-for="category in categories" :key="category['category_name']">
              <nuxt-link
                  @click="isVisible = false"
                  :to="`/category/${category['slug_category']}`"
              >
                {{ category['category_name'] }}
              </nuxt-link>
            </div>
          </el-col>
          <el-col :span="18" class="ml-12">
            <el-col :span="6">
              <div>
                <nuxt-link to="/category/smartphones">Smartphones</nuxt-link>
              </div>
              <div>
                <nuxt-link to="/category/smartphones">Smartphones</nuxt-link>
              </div>
              <div>
                <nuxt-link to="/category/smartphones">Smartphones</nuxt-link>
              </div>
              <div>
                <nuxt-link to="/category/smartphones">Smartphones</nuxt-link>
              </div>
              <div>
                <nuxt-link to="/category/smartphones">Smartphones</nuxt-link>
              </div>
            </el-col>
            <el-col :span="6">

            </el-col>
            <el-col :span="6">

            </el-col>
            <el-col :span="6">

            </el-col>
          </el-col>
        </el-row>
      </el-drawer>
    </ClientOnly>
  </div>
</template>
<style lang="scss" scoped>
.categories-select {
  position: relative;
}
</style>
