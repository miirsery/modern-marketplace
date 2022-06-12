<script lang="ts" setup>
const isLocationModalVisible  = ref(false)
const isCategoriesVisible = ref(false)

const toggleModal = (): void => {
    // ...
}

const toggleLocationModal = (): void => {
  isLocationModalVisible.value = !isLocationModalVisible.value
}

const toggleCategoriesVisible = (): void => {
  isCategoriesVisible.value = !isCategoriesVisible.value
}
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
            <div class="wrapper">
                 <common-header
                    @toggle-modal="toggleModal"
                    @open-location="toggleLocationModal"
                    @open-categories="toggleCategoriesVisible"
                />
                <slot></slot>
            </div>
        </div>
    </div>
</template>
