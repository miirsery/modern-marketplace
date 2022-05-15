<script setup lang="ts">
  import {useUserStore} from "~/store/user";

  const defaultAvatarPath = '../../assets/images/kuriyama.jpg'

  const emit = defineEmits([
    'toggleModal'
  ])

  const user = useUserStore()

  const handleToggleModal = () => {
      emit('toggleModal')
  }
</script>

<template>
  <div class="common-header">
    <div class="common-header__wrapper">
      <div class="common-header__logo">
        <nuxt-link to="/" >
          <img class="common-header__logo-link" src="../../assets/images/logo.svg" alt="logo" />
        </nuxt-link>
      </div>
      <ul class="common-header__menu d-flex">
        <li class="common-header__item mr-10">
          Account
        </li>
        <li class="common-header__item mr-10">
          Go to stars
        </li>
        <li class="common-header__item">
          <v-badge content='10' max='99' rounded="" color="primary">Cart</v-badge>
        </li>
      </ul>
      <v-avatar large class="common-header__avatar" @click="handleToggleModal">
       <img
           class="common-header__avatar-img"
           :src="user.user.avatar !== null
            && user.user.avatar !== undefined
            ? user.user.avatar
            : defaultAvatarPath"
            :alt="user.user.username"
       />
      </v-avatar>
    </div>
  </div>
</template>
<style scoped lang="scss">
.common-header {
  &__wrapper {
    display: flex;
    align-content: center;
    justify-content: space-between;
    padding: 20px 0;
  }

  &__logo {
    width: 40px;
  }

  &__avatar {
    width: 40px;
    height: 40px;

    &-img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
    }
  }
}
</style>