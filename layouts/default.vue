<script setup lang="ts">
import { storeToRefs, mapActions } from "pinia";
import { useCounterStore } from "~/store/filters";
import { useUserStore } from "~/store/user";
import { getCookie } from "~/utils/get-cookie";
import CommonLocation from "~/components/Common/CommonLocation.vue";


const main = useCounterStore()
const user = useUserStore()


const modalVisible = ref(false)
const categoriesDropdownVisible = ref(false)
const showCookies = ref(false)
const locationModalVisible = ref(false)

const { counter, name } = storeToRefs(main)

// const { addOne } = mapActions(useCounterStore, ['addOne'])
const { addOne } = main

function add(value: number) {

  main.$patch((state) => state.counter += value)
}

function reset() {
  main.$reset()
}

const toggleModal = () => {
  modalVisible.value = !modalVisible.value
}

const toggleDropdown = () => {
  categoriesDropdownVisible.value = !categoriesDropdownVisible.value
}

const toggleCookies = () => {
  showCookies.value = !showCookies.value
}

const toggleLocationModal = () => {
  locationModalVisible.value = !locationModalVisible.value
}

main.$subscribe((mutation, state) => {
  console.log(mutation)
})

const getUserData = () => {
  const matches = getCookie('user')
  if (!matches) return

  const userValuesData = []
  const userKeysData = []

  decodeURIComponent(matches[1]).split(',').forEach(item => {
    userKeysData.push(item.trim().split(': ').shift())
    userValuesData.push(item.trim().split(': ').pop())
  })

  const userData = Object.assign(userKeysData.map((item, index) => ({ [item]: userValuesData[index] })))
  setUserData(userData)
}

const setUserData = (userData) => {
  user.user.avatar = userData[0].avatar
  user.user.id = userData[1].id
  user.user.username = userData[2].username
  user.isAuthorized = true
}

onMounted(() => {
  getUserData()
  showCookies.value = localStorage.getItem('showCookie') !== 'true';
})


</script>
<template>
  <div class="inner">
    <div class="container">
      <div class="wrapper">
        <common-header
            @toggle-modal="toggleModal"
            @toggle-dropdown="toggleDropdown"
            @toggle-location-modal="toggleLocationModal"
        />
        <common-location v-if="locationModalVisible" />
        <categories-category-dropdown v-if="categoriesDropdownVisible" />
        <slot></slot>
        <auth-modal
            @toggle-modal="toggleModal"
            v-if="modalVisible
               && !user.isAuthorized"
        />
        <user-options v-if="user.isAuthorized && modalVisible" @toggle-modal="toggleModal" />
      </div>
    </div>
    <common-cookies v-if="showCookies" @close="toggleCookies" />
  </div>
</template>
<style scoped lang="scss">
.wrapper {
  position: relative;
}
.inner {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
}
</style>