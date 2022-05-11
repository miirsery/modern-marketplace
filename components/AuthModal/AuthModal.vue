<script setup lang="ts">
  import SignIn from "~/components/AuthModal/SignIn.vue";
  import SignUp from "~/components/AuthModal/SignUp.vue";

  const authMode= ref('SignIn')

  const authMods = {
    SignIn: 'SignIn',
    SignUp: 'SignUp',
  }

</script>
<template>
  <div class="auth-modal">
    <div class="auth-modal__wrapper">
      <div class="auth-modal__actions">
        <button
            v-for="(_, mode) in authMods"
            :key="mode"
            :class="['auth-modal__button', { active: authMode === mode }]"
            @click="authMode = mode"
          >
          {{ mode }}
        </button>
      </div>
      <div class="auth-modal__body">
        <sign-in v-if="authMode === 'SignIn'" />
        <sign-up v-else />
<!--        <component :is="authMods[authMode]"/>-->
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-modal {
  &__button {
    cursor: pointer;
  }
}
</style>