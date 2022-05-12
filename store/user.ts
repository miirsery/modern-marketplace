// store/user.ts
import { defineStore } from "pinia";
import axios from "axios";

const instance = axios.create({
    baseURL: "http://127.0.0.1:8000",
    withCredentials: false,
});

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            email: null,
            username: null,
            avatar: null,
        },
        isAuthorized: false,
    }),
    getters: {},
    actions: {
        // async signUp(data): Promise<void> {
        //     try {
        //         this.user = await fetch('http://localhost:8000//api/user/register/users/', {
        //             method: 'POST',
        //             body: JSON.stringify(data),
        //             headers: {
        //                 'Content-type': 'application/json; charset=UTF-8',
        //             },
        //             credentials: 'include',
        //         }).then(r => r.json())
        //     } catch (e) {
        //         console.log(e)
        //     }
        // },
        async signUp(data): Promise<void> {
            console.log(data)
            try {
                await instance.post('http://localhost:8000/api/user/register/users/', data)
            } catch (e) {
                console.log(e)
            }
        },
        async tokenCreate(data): Promise<any> {
            // return await fetch('http://localhost:8000/api/user/token-create', {
            //     method: 'POST',
            //     body: JSON.stringify(data),
            // }).then(r => r.json())

            await axios.post('http://localhost:8000/api/user/token-create', {
                data: data,
            })
        },

        async signIn(token: string): Promise<void> {
            await fetch('http://localhost:8000/api/user/authorization', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
        }
    }
})
