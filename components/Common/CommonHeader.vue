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
          <img src="" alt="logo" />
        </nuxt-link>
      </div>
      <ul class="common-header__menu">
        <li class="common-header__item">
          Account
        </li>
        <li class="common-header__item">
          Go to stars
        </li>
      </ul>
      <v-avatar large class="common-header__avatar" @click="handleToggleModal">
       <img
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
  }

  &__avatar {
    width: 40px;
    height: 40px;

    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
    }
  }
}
</style>