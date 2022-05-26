<script setup lang="ts">
const cities = [
    'Новосибирск',
    'Омск',
    'Москва',
    'Барнаул'
]

const emit = defineEmits([
    'closeModal'
])

const handleCloseModal = () => {
  emit('closeModal')
}

</script>

<template>
  <div class="common-location" @click="handleCloseModal">
    <div class="common-location__wrapper" @click.stop>
      <div class="common-location__top">
          <h2 class="common-location__title">Choose a city</h2>
          <div class="common-location__close" @click="handleCloseModal">X</div>
      </div>
      <input type="text" class="modal-input" placeholder="Start typing a city..."/>
      <ul class="common-location__content">
        <li class="common-location__city" v-for="city in cities" :key="city">
          {{ city }}
        </li>
      </ul>
    </div>
  </div>
</template>
<style scoped lang="scss">
.modal-input {}

.common-location {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  z-index: 100;
  background-color: $color-modal-overlay;

  &__wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300px;
    padding: 15px;
    z-index: 110;
    background-color: $color-modal-background;
    transform: translate(-50%, -50%);
  }

  &__top {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  &__close {
    cursor: pointer;
  }
}
</style>
