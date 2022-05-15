// store/user.ts
import { defineStore } from "pinia";
import {ProfileUserType, ResetPasswordType} from '@/types/user.type'

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            email: null,
            username: null,
            avatar: null,
            id: null,
        },
        isAuthorized: false,
    }),
    getters: {},
    actions: {
        async signUp(data): Promise<void> {
            this.user = await fetch('http://localhost:8000/api/user/register/users/', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(r => r.json())
        },

        async tokenCreate(data): Promise<{ token: string }> {
            return await fetch('http://localhost:8000/api/user/token-create/', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(r => r.json())
        },

        async signIn(token: string): Promise<ProfileUserType> {
            return await fetch('http://localhost:8000/api/user/authorization/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                }
            }).then(r => r.json())
        },

        async resetPassword(email: any): Promise<void> {
            try {
                await fetch('http://localhost:8000/api/user/register/users/reset_password/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({email: 'sania.nika@mail.ru'}),
                }).then(r => r.json())
            } catch (e) {
                console.log(e)
            }
        },

        async changeAvatar(data: any, token: any, userId: any): Promise<void> {
            try {
                await fetch(`/api/user/update/${userId}`, {
                    method: 'PUT',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'multipart/form-data',
                    },
                    body: data
                }).then(r => r.json())
            } catch (e) {
                console.log(e)
            }
        }
    }
})
