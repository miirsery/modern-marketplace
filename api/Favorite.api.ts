
import { AxiosService } from '@/api/axiosService'

class Favorite extends AxiosService {
    public addToFavorite(payload) {
        return this.axiosCall({
            method: 'post',
            url: `/api/product/favorite/add-product/`,
            data: payload
        })
    }
    public getTotalCountProductInFavorite() {
        return this.axiosCall({
            method: 'get',
            url: `/api/product/favorite/quantity-products/`,
        })
    }
}

export const favoriteApi = new Favorite()
