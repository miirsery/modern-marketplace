<script setup lang="ts">
  import { SignUpType } from "~/types/user.type";
  import {useUserStore} from "~/store/user";

  const user = useUserStore()

  const data = reactive<
      Partial<Omit<SignUpType,
          'username' | 'retryPassword'>>
      >({
    email: '',
    password: ''
  })

  const saveToken = (token: string): void => {
    //...
    // await signIn(token)
    document.cookie = token
  }

  const tokenCreate = async (): Promise<void> => {
   const token = await user.tokenCreate({
     email: data.email,
     password: data.password,
   })

    saveToken(token)
  }


  const handleSendData = async (): Promise<void> => {
    await tokenCreate()

    // await fetch('https://jsonplaceholder.typicode.com/posts', {
    //   method: 'POST',
    //   body: JSON.stringify({
    //     email: data.email,
    //     password: data.password,
    //   }),
    //   headers: {
    //     'Content-type': 'application/json; charset=UTF-8',
    //   },
    // })
    //     .then(r => r.json())
    //     .then(r => console.log(r))
  }

</script>
<template>
  <div class="sign-in">
    <form class="sign-in__from" @submit.prevent>
      <div class="sign-in__from-item modal-item">
        <label
            for="signInEmail"
            class="sign-in__input modal-label"
        >
          Email
        </label>
        <input
            type="text"
            id="signInEmail"
            v-model="data.email"
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