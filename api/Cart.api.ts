import {AxiosService} from "~/api/AxiosService";

class Cart extends AxiosService {
    public addToCart(payload, method) {
        return this.axiosCall({
            method: method,
            url: '/api/cart/add-product-in-cart/',
            data: payload
        })
    }

    public getAllProducts () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/list-products-cart/'
        })
    }
}

export const cartApi = new Cart()
