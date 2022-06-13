
import { AxiosService } from '@/api/axiosService'

class Auth extends AxiosService {
    public tokenCreate(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/user/token-create/',
            data: payload
        })
    }

    public signIn(token) {
        return this.axiosCall({
            method: 'get',
            url: '/api/user/authorization/',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
    }

    public signUp(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/user/register/users/',
            data: payload
        })
    }
}

export const authApi = new Auth()
