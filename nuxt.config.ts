import { defineNuxtConfig } from 'nuxt'
import svgLoader from 'vite-svg-loader'

export default defineNuxtConfig({
    ssr: false,
    css: [
        'element-plus/dist/index.css',
         '@/assets/style/main.scss'
    ],
    publicRuntimeConfig: {
        BASE_URL: process.env.BASE_URL,
    },
    buildModules: [
        '@pinia/nuxt',
    ],
    vite: {
        plugins: [svgLoader()],
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@import "@/assets/style/variables.scss";',
                },
            },
        },
    },
})
