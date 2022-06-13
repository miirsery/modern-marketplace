
import { AxiosService } from '@/api/axiosService'

class Categories extends AxiosService {
    public getCategories() {
        return this.axiosCall({
            method: 'get',
            url: '/api/product/list-category/',
        })
    }

    public getCategoryProducts(slug) {
        return this.axiosCall({
            method: 'get',
            url: `/api/product/catalog/${slug}/`,
        })
    }
}

export const categoriesApi = new Categories()
