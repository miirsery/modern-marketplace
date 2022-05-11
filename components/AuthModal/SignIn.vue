<script setup lang="ts">
  import { SignUpType } from "~/types/user.type";

  const data = reactive<
      Partial<Omit<SignUpType,
          'username' | 'retryPassword'>>
      >({
    email: '',
    password: ''
  })

  const handleSendData = async (): Promise<void> => {
    await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      body: JSON.stringify({
        email: data.email,
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
      <button
          class="sign-in__button modal-button"
          @click="handleSendData"
      >
        Submit
      </button>
    </form>
  </div>
</template>