<script lang="ts" setup>
import { useFavoriteStore } from "~/store/favorite";
import { useUserStore } from "~/store/user";
import { useCartStore } from "~/store/cart";

const isLocationModalVisible  = ref(false)
const isCategoriesVisible = ref(false)
const isAuthModalVisible = ref(false)

const favoriteStore = useFavoriteStore()
const user = useUserStore()
const cart = useCartStore()

const toggleModal = (): void => {
    // ...
}

const toggleLocationModal = (): void => {
  isLocationModalVisible.value = !isLocationModalVisible.value
}

const toggleCategoriesVisible = (): void => {
  isCategoriesVisible.value = !isCategoriesVisible.value
}

const toggleAuthModalVisible = (): void => {
  isAuthModalVisible.value = !isAuthModalVisible.value
}

onMounted(async () => {
  await user.aboutMe()
  await cart.getTotalProducts()
  await cart.getAllProducts()
  await favoriteStore.getTotalCountProductInFavorite()
})
</script>

<template>
    <div class="inner">
        <div class="container">
          <common-location
              :visible="isLocationModalVisible"
              @change-state="toggleLocationModal"
          />
          <lazy-categories-select
              :is-visible="isCategoriesVisible"
              @close-categories="toggleCategoriesVisible"
          />
          <lazy-user-auth
              :visible="isAuthModalVisible"
              @change-state="toggleAuthModalVisible"
          />
            <div class="wrapper">
                 <lazy-common-header
                    @toggle-modal="toggleModal"
                    @open-location="toggleLocationModal"
                    @open-categories="toggleCategoriesVisible"
                    @open-auth-modal="toggleAuthModalVisible"
                />
                <slot></slot>
            </div>
        </div>
    </div>
</template>
