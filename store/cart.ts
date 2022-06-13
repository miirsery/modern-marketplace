import {defineStore} from "pinia";
import {cartApi} from "~/api/Cart.api";

export const useCartStore = defineStore('cart', {
    state: () => ({
       products: []
    }),
    actions: {
        async addToCart(payload) {
            await cartApi.addToCart(payload)
        },
        async getAllProducts() {
            await cartApi.getAllProducts()
        }
    }
})
