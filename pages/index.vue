<script setup lang="ts">
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
    <common-header @toggle-modal="toggleModal"/>
</template>
    