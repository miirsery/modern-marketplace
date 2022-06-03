<script setup lang="ts">
import {useUserStore} from "~/store/user";
import {ResetPasswordType} from "~/types/user.type";
import {getCookie} from "~/utils/get-cookie";
import SuccessSendingEmail from "~/components/User/Dialogs/SuccessSendingEmail.vue";
const user = useUserStore()

const email = ref<ResetPasswordType>(null)
const avatar = ref(null)
const isVisible = ref(false)

// const token = getCookie('token')

const handleSendEmail = (): void => {
  isVisible.value = true
  // user.resetPassword({ email: email.value })
}

const handleFileUpload = (e): void => {
  avatar.value = e.target.files[0]
}

const handleSubmitFile = (): void => {
  const formData = new FormData()
  formData.append('username', user.user.username)
  formData.append('avatar', avatar.value)
  isVisible.value = true
  // user.changeAvatar(formData, token[1], user.user.id)
}

</script>
<template>
  <div class="user">
    <div id="users-settings">
      <form class="users-settings__form">
        <div class="mb-8 d-flex flex-md-column">
          <label for="users-settings-email">Enter email for reset password</label>
          <input
              id="users-settings-email"
              type="text"
              class="users-settings__input"
              placeholder="Your email..."
              v-model="email"/>
        </div>
        <v-btn class="mb-10" color="primary" depressed elevation="2" @click="handleSendEmail">
          Submit
        </v-btn>
      </form>
    </div>
    <div id="user-avatar">
      <form class="user-avatar__form">
        <input type="file" @change="handleFileUpload"/>
        <v-btn class="d-block" color="primary" depressed elevation="2" @click="handleSubmitFile">
          Submit
        </v-btn>
      </form>
    </div>
    <success-sending-email :visible="isVisible" @close="isVisible = false" />
  </div>
</template>
