import { defineStore } from "pinia";
import { favoriteApi } from "~/api/Favorite.api";
export const useFavoriteStore = defineStore('favorite', {
    state: () => ({
        count: 0,
        products: []
    }),
    getters: {
        hasFavoriteProduct: (state) => (productId) => state.products.some((product) => product.id === productId),
    },
    actions: {
        async addToFavorite(payload) {
            await favoriteApi.addToFavorite(payload)
        },
        async getProductsInFavorite () {
            const [_, data] = await favoriteApi.getProductsInFavorite()
            this.products = data
            this.count = data.length
        },
    }
})
