<script setup lang="ts">
const cities = [
    'Новосибирск',
    'Омск',
    'Москва',
    'Барнаул'
]

</script>

<template>
  <div class="common-location">
    <div class="common-location__wrapper">
     <h2 class="common-location__title">Choose a city</h2>
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
</style>