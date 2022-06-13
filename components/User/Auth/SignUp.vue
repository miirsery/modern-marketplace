<script lang="ts" setup>
import { authApi } from "~/api/Auth.api";
import {useUserStore} from "~/store/user";
const userStore = useUserStore()

const signUpForm = reactive({
  username: '',
  email: '',
  password: '',
  retryPassword: ''
})

const emit = defineEmits([
  'closeAuthModal'
])

const closeAuthModal = () => {
  emit('closeAuthModal')
}

const handleSignUp = async () => {
  try {
    await userStore.signUp({
      username: signUpForm.username,
      email: signUpForm.email,
      password: signUpForm.password
    })

    closeAuthModal()
  } catch (e) {
    console.log(e)
  }

}

</script>

<template>
  <el-form :model="signUpForm">
    <el-form-item>
      <el-input v-model="signUpForm.username" placeholder="Введите username" />
      <el-input v-model="signUpForm.email" placeholder="Введите email" />
      <el-input
          v-model="signUpForm.password"
          type="password"
          placeholder="Введите пароль"
          show-password
      />
      <el-input
          v-model="signUpForm.retryPassword"
          type="password"
          placeholder="Подтвердите пароль"
          show-password
      />
    </el-form-item>
    <el-button type="primary" @click="handleSignUp">Регистрация</el-button>
  </el-form>
</template>
