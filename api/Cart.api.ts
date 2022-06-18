import {AxiosService} from "~/api/AxiosService";

class Cart extends AxiosService {
    public addToCart(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/cart/add/',
            data: payload
        })
    }

    public getAllProducts () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/list-products-cart/'
        })
    }

    public updateCalculationsCart () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/update-calculations-cart/'
        })
    }
}

export const cartApi = new Cart()
