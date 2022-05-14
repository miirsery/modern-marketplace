<script setup lang="ts">
  import SignIn from "~/components/AuthModal/SignIn.vue";
  import SignUp from "~/components/AuthModal/SignUp.vue";

  const authMode= ref('SignIn')

  const emit = defineEmits([
    'toggleModal'
  ])

  const handleToggleModal = () => {
    emit('toggleModal')
  }

  const authMods = {
    SignIn: 'SignIn',
    SignUp: 'SignUp',
  }

</script>
<template>
  <div class="auth-modal" @click="handleToggleModal">
    <div class="auth-modal__wrapper" @click.stop>
      <div class="d-flex justify-space-between">
        <div class="d-flex justify-center">
          <button
              v-for="(_, mode) in authMods"
              :key="mode"
              :class="['auth-modal__button', { active: authMode === mode }]"
              @click="authMode = mode"
            >
            {{ mode }}
          </button>
        </div>
        <button class="auth-modal__close" @click="handleToggleModal">X</button>
      </div>
      <div class="auth-modal__body"  @close="handleToggleModal">
        <sign-in v-if="authMode === 'SignIn'" @toggle-modal="handleToggleModal" />
        <sign-up v-else />
<!--        <component :is="authMods[authMode]"/>-->
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-modal {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.2);

  &__wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    bottom: 0;
    right: 0;
    width: 40%;
    height: 30%;
    z-index: 110;
    background-color: #666666;
    padding: 15px;
    transform: translate(-50%, -50%);
  }

  &__button {
    cursor: pointer;
  }

  &__button {
    font-weight: 500;
    font-size: 18px;

    &.active {
      color: $color-accent;
    }

    &:first-child {
      margin: 0 2rem;
    }
  }
}
</style>