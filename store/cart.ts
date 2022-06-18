import {defineStore} from "pinia";
import {cartApi} from "~/api/Cart.api";

export const useCartStore = defineStore('cart', {
    state: () => ({
        products: [],
        count: 0,
    }),
    actions: {
        async addToCart (payload) {
            return await cartApi.addToCart(payload)
        },
        async getAllProducts () {
            return await cartApi.getAllProducts()
        },
        async updateCountProductsInCart (count){
            this.count = count
        },
        async updateCalculationsCart () {
            return await  cartApi.updateCalculationsCart()
        }
    }
})
