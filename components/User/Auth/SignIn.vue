<script lang="ts" setup>
import {useUserStore} from "~/store/user";
import Cookies from 'js-cookie'

const userStore = useUserStore()

const emit = defineEmits([
    'closeAuthModal'
])

const signInForm = reactive({
  username: '',
  password: '',
})

const clearForm = () => {
  signInForm.username = ''
  signInForm.password = ''
}

const closeAuthModal = () => {
  clearForm()

  emit('closeAuthModal')
}

const tokenCreate = async () => {
  await userStore.tokenCreate({
    username: signInForm.username,
    password: signInForm.password
  })
}

const signIn = async (token) => {
  await userStore.signIn(token)
  userStore.isAuthorized = true

  closeAuthModal()
}

const handleSubmit = async () => {
  try {
    await tokenCreate()

    const token = Cookies.get('token')

    await signIn(token)

  } catch (e) {
    console.log(e)
  }
}

</script>

<template>
  <el-form :model="signInForm">
    <el-form-item>
      <el-input v-model="signInForm.username" placeholder="Введите username" />
      <el-input
          v-model="signInForm.password"
          type="password"
          placeholder="Введите пароль"
          show-password
      />
    </el-form-item>
    <el-button type="primary" @click="handleSubmit">Авторизация</el-button>
  </el-form>
</template>
