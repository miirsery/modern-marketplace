
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
            method: 'put',
            url: `/api/cart/update-cart-products/${id}/`,
            data: count
        })
    }
}

export const productApi = new Product()
