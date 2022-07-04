import { defineStore } from "pinia";
import { favoriteApi } from "~/api/Favorite.api";
export const useFavoriteStore = defineStore('favorite', {
    state: () => ({
        count: 0,
        items: []
    }),
    getters: {},
    actions: {
        async addToFavorite(payload) {
            await favoriteApi.addToFavorite(payload)
        },
        async getTotalCountProductInFavorite () {
            const [_, data] = await favoriteApi.getTotalCountProductInFavorite()
            this.count = data.count_favorite_products
        },
        async getProductsInFavorite () {
            const [_, data] = await favoriteApi.getProductsInFavorite()
            for (let item of data) {
                this.items.push(item)
            }
        },
    }
})
