// store/user.ts
import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            email: null,
            username: null,
            avatar: null,
        }
    }),
    getters: {},
    actions: {
        async signUp(data) {
            try {
                this.user = await fetch('https://jsonplaceholder.typicode.com/posts', {
                    method: 'POST',
                    body: JSON.stringify(data),
                    headers: {
                        'Content-type': 'application/json; charset=UTF-8',
                    },
                })
                    .then(r => r.json())
                console.log(this.user)
            } catch (e) {
                console.log(e)
            }
        }
    }
})
