import {defineStore} from "pinia";

export const useCartStore = defineStore('cart', {
    state: () => ({
        books: []
    }),
    actions: {
        async addToCart(payload): Promise<any> {
            // return await fetch(`http://localhost:8000/api/user/token-create/`, {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: payload
            // }).then(r => r.json())
        }
    }
})
