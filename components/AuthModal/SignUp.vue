<script setup lang="ts">
  import { SignUpType } from "~/types/user.type";
  import { validatePassword } from "~/utils/validate-data";

  const data = reactive<SignUpType>({
    email: '',
    username: '',
    password: '',
    retryPassword: ''
  })


  const handleSendData = async (): Promise<void> => {
    if(!validatePassword(data.password, data.retryPassword)) {
      console.error('Incorrect data')
      return
    }

    await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      body: JSON.stringify({
        email: data.email,
        username: data.username,
        password: data.password,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
    .then(r => r.json())
    .then(r => console.log(r))
  }

</script>
<template>
  <div class="sign-up">
    <form class="sign-up__from" @submit.prevent>
      <div class="sign-up__from-item modal-item">
        <label
            for="signUpEmail"
            class="sign-up__input modal-label"
        >
          Email
        </label>
        <input
            type="text"
            id="signUpEmail"
            v-model="data.email"
            class="sign-up__input modal-input"
            placeholder="Enter an email..."
        />
      </div>
      <div class="sign-up__from-item modal-item">
        <label
            for="signUpUsername"
            class="sign-up__input modal-label"
        >
          Username
        </label>
        <input
            type="text"
            id="signUpUsername"
            v-model="data.username"
            class="sign-up__input modal-input"
            placeholder="Enter an email..."
        />
      </div>
      <div class="sign-up__from-item modal-item">
        <label
            for="signUpPassword"
            class="sign-up__input modal-label"
        >
          Password
        </label>
        <input
            type="password"
            id="signUpPassword"
            v-model="data.password"
            class="sign-up__input modal-input"
            placeholder="Enter an password..."
        />
      </div>
      <div class="sign-up__from-item modal-item">
        <label
            for="signUpRetryPassword"
            class="sign-up__input modal-label"
        >
          Password
        </label>
        <input
            type="password"
            id="signUpRetryPassword"
            v-model="data.retryPassword"
            class="sign-up__input modal-input"
            placeholder="Enter an password..."
        />
      </div>
      <button
          class="sign-up__button modal-button"
          @click="handleSendData"
      >
        Submit
      </button>
    </form>
  </div>
</template>