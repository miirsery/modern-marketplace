
import { AxiosService } from '@/api/axiosService'
const token = 'fede71f2df7a3314f6a6b8de7b7e8e3f420157be';

class SearchCities extends AxiosService {
    public getCities(payload) {
        return this.axiosCall({
            method: 'post',
            url: 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address',
            headers: {
                "Authorization": "Token " + token
            },
            data: payload
        })
    }
}

export const searchCitiesApi = new SearchCities()
