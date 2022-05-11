<script setup lang="ts">
    import AuthModal from "~/components/AuthModal/AuthModal.vue";

    useMeta({
        title: `Main page`,
        meta: [
            {
                name: "viewport",
                content: "width=device-width",
            },
        ],
    })

    const authModalVisible = ref(false)

    const toggleModal = () => {
      authModalVisible.value = !authModalVisible.value
    }
</script>
    
<template>
    <div class="nuxt__container">
      <common-header @toggle-modal="toggleModal"/>
      <auth-modal v-if="authModalVisible" />
    </div>
</template>
    