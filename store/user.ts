import { defineStore } from "pinia";
import { authApi } from "~/api/Auth.api";
import Cookies from 'js-cookie'

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            username: null,
            avatar: null,
            id: null,
        },
        isAuthorized: false,
    }),
    getters: {},
    actions: {
        async signUp(payload) {
           await authApi.signUp(payload)
        },
        async tokenCreate(payload) {
            const [_, token] = await authApi.tokenCreate(payload)
            Cookies.set('token', token.token)
        },
        async signIn(token) {
            const [_, data] = await authApi.signIn(token)
            this.user = data
        },
        async aboutMe() {
            const [_, data] = await authApi.aboutUser()
            this.user = data
        }
    }
})
