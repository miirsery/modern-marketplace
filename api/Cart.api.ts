import {AxiosService} from "~/api/AxiosService";

class Cart extends AxiosService {
    public addToCart(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/cart/add-product-in-cart/',
            data: payload
        })
    }

    public updateProductCount(payload) {
        return this.axiosCall({
            method: 'patch',
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

    public updateCalculationsCart () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/update-calculations-cart/'
        })
    }
    public getTotalProducts () {
        return this.axiosCall({
            method: 'get',
            url: '/api/cart/total-count-products/'
        })
    }
}

export const cartApi = new Cart()
