<script setup lang="ts">
const emit = defineEmits([
    'close'
])

const closeCookies = () => {
  emit('close')
}


const handleAcceptCookies = (): void => {
  localStorage.setItem('showCookie', 'true')
  closeCookies()
  ///
}

const handleDenyCookies = (): void => {
  ///
  closeCookies()
}
</script>

<template>
  <div class="common-cookies bg-amber-darken-4 d-flex justify-lg-space-between pl-15 pr-15 align-center">
    <v-avatar class="common-cookies__icon">
      <img src="../../assets/icons/cookies.svg" alt="cookies">
    </v-avatar>
    <p class="common-cookies__text">We use cookies</p>
    <div class="common-cookies__buttons pt-3 mb-3">
      <v-btn flat class="bg-white pr-2 pl-2 mr-5" @click="handleAcceptCookies">
        Accept
      </v-btn>
      <v-btn flat class="bg-white pr-2 pl-2" @click="handleDenyCookies">
        Deny
      </v-btn>
    </div>
  </div>
</template>

<style scoped lang="scss">
.common-cookies {
  &__icon {
    width: 60px;
    height: 60px;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}
</style>