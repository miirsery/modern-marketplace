<script lang="ts" setup>
import {useUserStore} from "~/store/user";

const userStore = useUserStore()
const username = computed(() => userStore.user.username)
const id = computed(() => userStore.user.id)

const oldPassword = ref()
const newPawssword = ref()
const avatar = ref(null)

const selectedFile = ref(null)


const handleSubmit = (value) => {
  selectedFile.value = value.raw
  const form = new FormData()
  form.append('avatar', value.raw, value.raw.name)
  form.append('username', username.value)

  userStore.changeAvatar(form, id.value)
}
</script>
<template>
<div class="profile">
  <el-input v-model="oldPassword" placeholder="Enter old password..." />
  <el-input v-model="newPawssword" placeholder="Enter new password..." />
  <el-button type="primary">Подтвердить</el-button>
  <el-upload
      v-model="avatar"
      :auto-upload="false"
      action="#"
      @change="handleSubmit"
  >
    <template #trigger>
      <el-button type="primary">select file</el-button>
    </template>
    <el-button @click="handleSubmit">
      Save
    </el-button>
  </el-upload>
</div>
</template>
