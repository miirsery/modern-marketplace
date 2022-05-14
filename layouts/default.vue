<script setup lang="ts">
import { storeToRefs, mapActions } from "pinia";
import { useCounterStore } from "~/store/filters";
import { useUserStore } from "~/store/user";
import UserOptions from "~/components/User/UserOptions.vue";
const main = useCounterStore()
const user = useUserStore()


const modalVisible = ref(false)
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

main.$subscribe((mutation, state) => {
  console.log(mutation)
})

const getCookie =  (name): void => {
  const matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));

  if (!document.cookie || !matches) return

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
  getCookie('user')
})


</script>
<template>
    <div class="container">
        <common-header @toggle-modal="toggleModal" />
        <slot></slot>
        <auth-modal
              @toggle-modal="toggleModal"
              v-if="modalVisible
               && !user.isAuthorized"
          />
       <user-options v-if="user.isAuthorized && modalVisible" @toggle-modal="toggleModal" />
    </div>
</template>
<style scoped lang="scss">
.container {
  margin: 0 auto;
  padding: 0 15px;
  max-width: 1410px;
}
</style>