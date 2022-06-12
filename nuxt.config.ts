import { defineNuxtConfig } from 'nuxt'

export default defineNuxtConfig({
    css: [
        'element-plus/dist/index.css',
         '@/assets/style/main.scss'
    ],
    // env: {
    //     baseUrl: process.env.BASE_URL || 'http://localhost:3000'
    // },
    publicRuntimeConfig: {
        BASE_URL: process.env.BASE_URL,
    },
    vite: {
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@import "@/assets/style/variables.scss";',
                },
            },
        },
    },
})
