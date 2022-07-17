import {defineStore} from "pinia";
import {cartApi} from "~/api/Cart.api";

export const useCartStore = defineStore('cart', {
    state: () => ({
        products: [],
        count: 0,
    }),
    getters: {
        getAllProductsInCart: (state): any => state.products,
        getProduct: (state) => (productId) => state.products.find((item) => item['product_name'].id === productId),
        hasProduct: (state) => (productId) => state.products.some((product) => product['product_name'].id === productId),
        isLoaded: (state) => state.products.length > 0,
    },
    actions: {
        async addToCart (payload) {
            return await cartApi.addToCart(payload)
        },
        async updateCount (payload) {
            const [error, data] = await cartApi.updateCount(payload)
            this.count = data.count_products_in_basket
        },
        async getAllProducts () {
            const [error, data] = await cartApi.getAllProducts()
            this.products = data.products
            this.count = data.total_products
        },
        async updateCountProductsInCart (count){
            this.count = count
        },
        async removeProduct (id: number | string) {
            const [error, data] = await cartApi.removeProduct(id)
            this.count = data.count_products_in_basket
        }
    }
})
