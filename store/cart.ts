import {defineStore} from "pinia";
import {cartApi} from "~/api/Cart.api";

export const useCartStore = defineStore('cart', {
    state: () => ({
        products: [],
        count: 0,
    }),
    getters: {
        getAllProductsInCart: (state): any => state.products,
        getCountProductsInCart: (state) => state.products.length,
        hasProduct: (state) => (productId) => state.products.some((product) => product.id === productId),
        isLoaded: (state) => state.products.length > 0,
    },
    actions: {
        async addToCart (payload, method) {
            return await cartApi.addToCart(payload, method)
        },
        // async updateProductCount (payload) {
        //     return await cartApi.updateProductCount(payload)
        // },
        async getAllProducts () {
            const [error, data] = await cartApi.getAllProducts()
            this.products = data.products
            this.count = data.total_products
        },
        async updateCountProductsInCart (count){
            this.count = count
        },
    }
})
