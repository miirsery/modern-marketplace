import {defineStore} from "pinia";
import {categoriesApi} from "~/api/Categories.api";

export const useCategoryProducts = defineStore('categoryProducts', {
    state: () => ({
        products: [],
        count: 0,
    }),
    getters: {
        getAllCategoryProducts: (state): any => state.products,
        getCountProductsInCart: (state) => state.products.length,
        hasProduct: (state) => (productId) => state.products.some((product) => product.id === productId),
        isLoaded: (state) => state.products.length > 0,
    },
    actions: {
        async getCategoryProducts(payload) {
            const [error, data] = await categoriesApi.getCategoryProducts(payload)
            this.products = data
        }
    }
})
