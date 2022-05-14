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
  <div class="user-options">
    <div class="user-options__wrapper">
      <v-list>
        <v-list-item
            v-for="(item, i) in items"
            :key="i"
        >
          <v-list-item-title>
            <nuxt-link
                class="text-blue-accent-4 user-options__link"
                :to="`/user#${item.slug}`"
                @click="handleToggleModal"
            >
              {{ item.title }}
            </nuxt-link>
          </v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title @click="handleLogout">Выход</v-list-item-title>
        </v-list-item>
      </v-list>
    </div>
  </div>
</template>

<style scoped lang="scss">
.user-options {
  &__link {
    text-decoration: none;
  }
}
</style>