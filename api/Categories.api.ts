
import { AxiosService } from '@/api/axiosService'

class Categories extends AxiosService {
    public getCategories() {
        return this.axiosCall({
            method: 'get',
            url: '/api/product/list-category/',
        })
    }
}

export const categoriesApi = new Categories()
