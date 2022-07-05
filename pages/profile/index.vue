<script lang="ts" setup>
const oldPassword = ref()
const newPawssword = ref()
const avatar = ref(null)

</script>
<template>
<div class="profile">
  <el-input v-model="oldPassword" placeholder="Enter old password..." />
  <el-input v-model="newPawssword" placeholder="Enter new password..." />
  <el-button type="primary">Подтвердить</el-button>
  <el-upload
      v-model="avatar"
  >
    <el-button>
      Click to upload
    </el-button>
  </el-upload>
</div>
</template>
