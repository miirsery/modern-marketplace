<script setup lang="ts">
  const emit = defineEmits([
    'toggleModal'
  ])

  const handleToggleModal = () => {
      emit('toggleModal')
  }
</script>

<template>
  <div class="common-header">
    <div class="common-header__logo">
      <img src="" alt="logo" />
    </div>
    <ul class="common-header__menu">
      <li class="common-header__item">
        Account
      </li>
      <li class="common-header__item">
        Go to stars
      </li>
    </ul>
    <div class="common-header__avatar" @click="handleToggleModal">
      <img src="" alt="avatar">
    </div>
  </div>
</template>