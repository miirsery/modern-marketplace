import {AxiosService} from "~/api/AxiosService";

class Cart extends AxiosService {
    public addToCart(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/cart/add-product-in-cart/',
            data: payload
        })
    }

    public updateCount(payload) {
        return this.axiosCall({
            method: 'patch',
            url: '/api/cart/update-count-products-no-directly-cart/',
            data: payload
        })
    }

    public getAllProducts () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/list-products-cart/'
        })
    }

    public removeProduct (id: number | string) {
        return this.axiosCall({
            method: 'post',
            url: '/api/cart/delete-product-in-cart/',
            data: {
                product_id: id
            }
        })
    }
}

export const cartApi = new Cart()
