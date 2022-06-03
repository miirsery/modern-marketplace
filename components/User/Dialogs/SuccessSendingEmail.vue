<script lang="ts" setup>
import {onMounted} from "@vue/runtime-core";

const prop = defineProps({
  visible: Boolean
})

const emit = defineEmits(['close'])

const handleVisibleChange = (): void => {
  emit('close')
}

</script>

<template>
  <v-dialog
      v-model="prop.visible"
      max-width="290"
      @click="handleVisibleChange"
  >
    <v-card @click.stop>
      <v-card-title class="text-h5">
        The confirmation code has been sent to the post office
      </v-card-title>

      <v-card-text>
        On { this email }
      </v-card-text>

      <v-btn
          color="green darken-1"
          text
          @click="handleVisibleChange"
      >
        Agree
      </v-btn>
    </v-card>
  </v-dialog>
</template>
