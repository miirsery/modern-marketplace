<script setup lang="ts">
import {ProfileUserType, SignUpType} from "~/types/user.type";
  import {useUserStore} from "~/store/user";

  const emit = defineEmits([
    'toggleModal'
  ])

  const closeModal = (): void => {
    emit('toggleModal')
  }

  const user = useUserStore()

  const data = reactive<
      Partial<Omit<SignUpType,
          'email' | 'retryPassword'>>
      >({
    username: '',
    password: ''
  })

  const safeStateInCookie = (avatar, id, username): void => {
    if (!navigator.cookieEnabled) return
    document.cookie = `user=avatar: ${avatar}, id: ${id}, username: ${username}`
  }

  const setUserData = (data: ProfileUserType): void => {
    user.user.avatar = data.avatar
    user.user.id = data.id
    user.user.username = data.username

    safeStateInCookie(data.avatar, data.id, data.username)
  }

  const signIn = async (token: string): Promise<void> => {
    const userData = await user.signIn(token)

    setUserData(userData)

    user.isAuthorized = true

    closeModal()
  }

  const saveToken = async (token: { token: string }): Promise<void> => {
    document.cookie = `token=${(token.token)}`

    await signIn(token.token)
  }

  const tokenCreate = async (): Promise<void> => {
   const token = await user.tokenCreate({
     username: data.username,
     password: data.password,
   })

    await saveToken(token)
  }


  const handleSendData = async (): Promise<void> => {
    await tokenCreate()
  }

</script>
<template>
  <div class="sign-in">
    <form class="sign-in__from" @submit.prevent>
      <div class="sign-in__from-item modal-item">
        <label
            for="signInUsername"
            class="sign-in__input modal-label"
        >
          Username
        </label>
        <input
            type="text"
            id="signInUsername"
            v-model="data.username"
            class="sign-in__input modal-input"
            placeholder="Enter an email..."
        />
      </div>
      <div class="sign-in__from-item modal-item">
        <label
            for="signInPassword"
            class="sign-in__input modal-label"
        >
          Password
        </label>
        <input
            type="password"
            id="signInPassword"
            v-model="data.password"
            class="sign-in__input modal-input"
            placeholder="Enter an password..."
        />
      </div>
      <v-btn
          class="sign-in__button modal-button"
          @click="handleSendData"
      >
        Submit
      </v-btn>
    </form>
  </div>
</template>