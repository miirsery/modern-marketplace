<script setup lang="ts">
import {useUserStore} from "~/store/user";
import {ResetPasswordType} from "~/types/user.type";

const email = ref<ResetPasswordType>(null)
const user = useUserStore()

const handleSendEmail = (): void => {
  user.resetPassword({ email: email.value })
}

</script>
<template>
  <div class="user">
    <div id="users-settings">
      <form class="users-settings__form">
        <div class="mb-8 d-flex flex-md-column">
          <label for="users-settings-email modal-label">Enter email for reset password</label>
          <input
              id="users-settings-email"
              type="text"
              class="users-settings__input"
              placeholder="Your email..."
              v-model="email"/>
        </div>
        <v-btn color="primary" depressed elevation="2" @click="handleSendEmail">
          Submit
        </v-btn>
      </form>
    </div>
  </div>
</template>