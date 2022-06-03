<script setup lang="ts">
import {onMounted} from "@vue/runtime-core";


const cities = ref([])
const emit = defineEmits([
    'closeModal'
])

const handleCloseModal = () => {
  emit('closeModal')
}

const url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address";
const token = 'fede71f2df7a3314f6a6b8de7b7e8e3f420157be';
const query = ref('');

const options = {
  method: "POST",
  mode: "cors",
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Token " + token
  },
  body: JSON.stringify({query: query.value})
};

const getCities = async (): Promise<any> => {
  return fetch(url, {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": "Token " + token
    },
    body: JSON.stringify({query: query.value})
  })
      .then(response => response.json())
      .then(result => {
        cities.value = result.suggestions
      })
      .catch(error => console.log("error", error));
}

watch(() => query.value,
    async () => {
      await getCities()
    }
)

onMounted(async (): Promise<void> => {
  await getCities()
})

</script>

<template>
  <div class="common-location" @click="handleCloseModal">
    <div class="common-location__wrapper" @click.stop>
      <div class="common-location__top">
          <h2 class="common-location__title">Choose a city</h2>
          <div class="common-location__close" @click="handleCloseModal">X</div>
      </div>
      <input
          v-model="query"
          type="text"
          class="modal-input"
          placeholder="Start typing a city..."
      />
      <ul class="common-location__content">
        <li class="common-location__city" v-for="city in cities" :key="city">
          {{ city.value }}
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
