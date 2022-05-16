<script setup lang="ts">
  import {useUserStore} from "~/store/user";

  const defaultAvatarPath = '../../assets/images/kuriyama.jpg'

  const emit = defineEmits([
    'toggleModal',
    'toggleDropdown',
    'toggleLocationModal'
  ])

  const user = useUserStore()

  const handleToggleModal = (): void => {
      emit('toggleModal')
  }

  const handleToggleDropdown = (): void => {
    emit('toggleDropdown')
  }

  const handleToggleLocationModal = (): void => {
      emit('toggleLocationModal')
  }
</script>

<template>
  <header class="common-header">
    <div class="common-header__top mb-1 mt-2 d-flex align-center">
      <nav class="common-header__navigation">
        <ul class="common-header__menu">
          <li class="common-header__item d-flex align-center">
            <button class="common-header__location d-flex align-center" type="button" @click="handleToggleLocationModal">
              <img class="common-header__icon-small" src="../../assets/icons/location.svg" alt="location" />
              Новосибирск
            </button>
          </li>
        </ul>
      </nav>
    </div>
    <div class="common-header__bottom">
      <div class="common-header__start d-flex align-center">
        <nuxt-link to="/" >
          <img class="common-header__logo" src="../../assets/images/logo.svg" alt="logo" />
        </nuxt-link>
        <v-btn color="primary" class="pl-2 pr-2 ml-4" @click="handleToggleDropdown">
          Catalog
        </v-btn>
      </div>
      <common-search />
      <ul class="common-header__menu">
        <li class="common-header__item mr-10 d-flex flex-column align-center">
          <nuxt-link to="/cart">
            <v-badge content='2' max='99' rounded="" color="primary">
              <img class="common-header__icon" src="../../assets/icons/cart-icon.svg" alt="cart">
            </v-badge>
            <p class="common-header__item-text">Корзина</p>
          </nuxt-link>
        </li>
        <li class="common-header__item mr-10 d-flex flex-column align-center">
          <nuxt-link to="/orders">
            <v-badge content='10' max='99' rounded="" color="primary">
              <img class="common-header__icon" src="../../assets/icons/orders-icon.svg" alt="order">
            </v-badge>
            <p class="common-header__item-text">Заказы</p>
          </nuxt-link>
        </li>
        <li class="common-header__item mr-10 d-flex flex-column align-center">
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
          <p class="common-header__item-text">Профиль</p>
        </li>
      </ul>
    </div>
  </header>
</template>
<style scoped lang="scss">
.common-header {
  &__bottom {
    display: flex;
    align-content: center;
    justify-content: space-between;
    padding: 20px 0;
  }

  &__logo {
    width: 40px;
  }

  &__item {
    text-align: center;
    cursor: pointer;
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

  &__menu {
    display: flex;
    align-items: center;
  }

  &__bottom {
    align-items: center;
  }

  &__icon {
    width: 40px;

    &-small {
      width: 16px;
      height: 16px;
    }
  }
}
</style>