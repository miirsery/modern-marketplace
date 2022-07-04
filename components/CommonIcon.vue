<script lang="ts" setup>
type IconSizeType = 'x-small' | 'small' | 'default' | 'large' | 'x-large'

interface IIconComponentProps {
  isStroked?: boolean
  svg: string
  color?: any
  size?: IconSizeType | number,
  className: string
}

const props = withDefaults(defineProps<IIconComponentProps>(), {
  size: 20,
})

const dynamicSvg = ref(null)

const importSvg = async (svgText: string) => {
  if (svgText) {
    return await import(`../assets/icons/${svgText}.svg`)
  }
}

watch(
    () => props.svg,
    async (svgText) => {
      dynamicSvg.value = await importSvg(svgText)
    }
)

onMounted(async () => {
  dynamicSvg.value = await importSvg(props.svg)
})
</script>
<template>
  <component :is="dynamicSvg" v-if="dynamicSvg" class="nuxt-icon" :class="props.className"></component>
</template>
