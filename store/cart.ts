import {defineStore} from "pinia";
import {cartApi} from "~/api/Cart.api";

export const useCartStore = defineStore('cart', {
    state: () => ({
        products: [],
        count: 0,
    }),
    getters: {
        getAllProductsInCart: (state): any => state.products,
        hasProduct: (state) => (productId) => state.products.some((product) => product.id === productId),
        isLoaded: (state) => state.products.length > 0
    },
    actions: {
        async addToCart (payload) {
            return await cartApi.addToCart(payload)
        },
        async updateProductCount (payload) {
            return await cartApi.updateProductCount(payload)
        },
        async getAllProducts () {
            const [error, data] = await cartApi.getAllProducts()
            this.products = data.products
        },
        async updateCountProductsInCart (count){
            this.count = count
        },
        async updateCalculationsCart () {
            return await cartApi.updateCalculationsCart()
        },
        async getTotalProducts () {
            const [error, data] = await cartApi.getTotalProducts()
            this.count = data.count_products_in_basket
        }
    }
})
