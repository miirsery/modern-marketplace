
import { AxiosService } from '@/api/axiosService'

class Product extends AxiosService {
    public getProduct(slug) {
        return this.axiosCall({
            method: 'get',
            url: `/api/product/v1/product-info/${slug}/`,
        })
    }
    public updateCountCurrentProductInCart (id: number, count: number) {
        return this.axiosCall({
            method: 'post',
            url: `/api/cart/update-calculations-cart/${id}/`,
            data: count
        })
    }
}

export const productApi = new Product()
