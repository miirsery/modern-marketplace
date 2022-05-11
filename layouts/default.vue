<script setup lang="ts">
  const authModalVisible = ref(false)

  const toggleModal = () => {
    authModalVisible.value = !authModalVisible.value
  }

</script>
<template>
    <div class="container">
        <common-header @toggle-modal="toggleModal"/>
        <slot></slot>
        <auth-modal @toggle-modal="toggleModal" v-if="authModalVisible" />
    </div>
</template>