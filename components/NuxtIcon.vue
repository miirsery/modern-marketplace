<script lang="ts" setup>
const props = defineProps({
  name: {
      type: String,
      required: true,
    },
    width: {
      type: [Number, String],
      default: 14,
    },
    height: {
      type: [Number, String],
      default: 14,
    },
    newClass: {
      type: String,
      default: null,
    },
})

const data = reactive({
    href: computed(() => `#${props.name}`),
    iconClass: computed(() => `nuxt-icon--${props.name}`),
})

</script>

<template>
  <svg
    class="nuxt-icon"
    :class="[data.iconClass, newClass]"
    :width="width"
    :height="height"
    aria-hidden="true"
  >
    <use xmlns:xlink="http://www.w3.org/1999/xlink" :xlink:href="data.href" />
  </svg>
</template>



<style lang="scss" scoped>
.app-icon {
  position: relative;
  display: inline-block;
  flex-shrink: 0;
}
</style>
