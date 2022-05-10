import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    app: {
      head: {
          meta: [
              { charset: 'utf-8'  },
              { name: 'viewport', content: 'width=device-width, initial-scale=1' },
              { name: 'format-detection', content: 'telephone=no' }
          ]
      }
    },
    dirs: [
        "~/components"
    ],
    css: [
        '@/styles/main.scss'
    ],
})
