<script setup lang="ts">
import {useUserStore} from "~/store/user";

const user = useUserStore()

const emit = defineEmits([
  'toggleModal'
])

const items = [
  { title: 'Настройки', slug: 'user-settings' },
  { title: 'Сообщения', slug: 'user-messages' },
  { title: 'Корзина', slug: 'user-cart' },
]

const handleToggleModal = () => {
  emit('toggleModal')
}

const clearCookies = () => {
  const cookies = document.cookie.split(";");

  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i];
    const eqPos = cookie.indexOf("=");
    const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
  }
}

const handleLogout = () => {
  user.isAuthorized = false
  user.user ={
    email: null,
      username: null,
      avatar: null,
      id: null,
  }

  clearCookies()
  handleToggleModal()

  document.location.reload()
}

</script>

<template>
  <nav class="user-options">
    <ul class="user-options__menu">
      <li
          class="mb-5"
          v-for="(item, i) in items"
          :key="i"
      >
        <nuxt-link
            class="text-blue-accent-4 user-options__link"
            :to="`/user#${item.slug}`"
            @click="handleToggleModal"
        >
          {{ item.title }}
        </nuxt-link>
      </li>
      <li @click="handleLogout">Выход</li>
    </ul>
  </nav>
</template>

<style scoped lang="scss">
.user-options {
  &__menu {
    position: absolute;
    z-index: 120;
    right: 0;
    top: 80px;
    width: 200px;
    background-color: rgba(0, 0, 0, 0.3);
  }

  &__link {
    text-decoration: none;
  }

  &__menu {
    z-index: 130;
  }
}
</style>