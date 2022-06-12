<script lang="ts" setup>
const props = defineProps({
  visible: {
    type: Boolean,
  }
})

const emit = defineEmits([
    'changeState'
])

const searchValue = ref('')
const query = ref('');
const cities = ref([
    'Москва',
    'Питер',
    'Омск'
])

const handleChangeState = () => {
  emit('changeState')
}

const getCities = async (): Promise<any> => {
  return fetch(url, {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": "Token " + token
    },
    body: JSON.stringify({query: searchValue.value})
  })
      .then(response => response.json())
      .then(result => {
        cities.value = result.suggestions
      })
      .catch(error => console.log("error", error));
}

watch(() => searchValue.value,
    async () => {
      await getCities()
    }
)

const url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address";
const token = 'fede71f2df7a3314f6a6b8de7b7e8e3f420157be';

</script>

<template>
  <ClientOnly>
    <el-dialog
        v-model="visible"
        title="Choose a city"
        width="30%"
        @close="handleChangeState"
    >
      <el-input placeholder="Начните поиск города" v-model="searchValue" />
      <ul class="common-location__content">
        <li class="common-location__city" v-for="city in cities" :key="city">
          {{ city.value }}
        </li>
      </ul>
    </el-dialog>
  </ClientOnly>
</template>
