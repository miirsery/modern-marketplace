<script lang="ts" setup>
import SignIn from "~/components/User/Auth/SignIn.vue";
import SignUp from "~/components/User/Auth/SignUp.vue";

const props = defineProps({
  visible: {
    type: Boolean,
  }
})

const authType = ref('SignIn')

const authMods = {
  SignIn: 'SignIn',
  SignUp: 'SignUp',
}

const emit = defineEmits([
  'changeState'
])

const handleChangeState = () => {
  emit('changeState')
}
</script>

<template>
  <ClientOnly>
    <div class="user-auth-modal">
      <el-dialog
        v-model="visible"
        width="30%"
        @close="handleChangeState"
      >
        <template #header="{ titleId, titleClass }">
         <h2 class="user-auth-modal__title">
           <el-button
               v-for="(_, mode) in authMods"
               :key="mode"
               :class="['user-auth-modal__type', { active: authType === mode }]"
               @click="authType = mode"
           >
              {{ mode }}
           </el-button>
         </h2>
        </template>
        <div class="user-auth-modal__body">
          <sign-in v-if="authType === 'SignIn'" />
          <sign-up v-else />
        </div>
      </el-dialog>
    </div>
  </ClientOnly>
</template>
<style scoped lang="scss">
.user-auth-modal {
  &__type {
    background: none;
    border: none;
    outline: none;
    padding: 0;

    &:hover,
    &:focus,
    &:focus-visible{
      background: none;
      border: none;
      outline: none;
    }

    &.active {
      border-bottom: 1px solid $color-accent;
    }
  }
}
</style>
