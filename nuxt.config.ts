import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    app: {
      head: {
          htmlAttrs: {
              lang: 'en'
          },
          meta: [
              { charset: 'utf-8' },
              { name: 'viewport', content: 'width=device-width, initial-scale=1' },
              { hid: 'description', name: 'description', content: '' },
              { name: 'format-detection', content: 'telephone=no' }
          ]
      }
    },
    dirs: [
        "~/components"
    ],
    components: true,
})
