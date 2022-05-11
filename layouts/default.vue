<script setup lang="ts">
import { storeToRefs, mapActions } from "pinia";
import { useCounterStore } from "~/store/filters";
import { useUserStore } from "~/store/user";
const main = useCounterStore()
const user = useUserStore()


const authModalVisible = ref(false)
const { counter, name } = storeToRefs(main)

// const { addOne } = mapActions(useCounterStore, ['addOne'])
const { addOne } = main

function add(value: number) {
  // main.$patch({
  //   counter: counter.value + value
  // })

  main.$patch((state) => state.counter += value)
}

function reset() {
  main.$reset()
}

const toggleModal = () => {
  authModalVisible.value = !authModalVisible.value
}

main.$subscribe((mutation, state) => {
  console.log(mutation)
})

</script>
<template>
    <div class="container">
      <button type="button" @click="reset">Reset</button>
      <button type="button" @click="add(15)">Click me</button>
      {{ counter }}
        <common-header @toggle-modal="toggleModal"/>
        <slot></slot>
        <auth-modal
            @toggle-modal="toggleModal"
            v-if="authModalVisible
             && !user.isAuthorized"
        />
    </div>
</template>