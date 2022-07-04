
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
        })
    }

    public signUp(payload) {
        return this.axiosCall({
            method: 'post',
            url: '/api/user/register/users/',
            data: payload
        })
    }

    public aboutUser() {
        return this.axiosCall({
            method: 'get',
            url: '/api/user/me'
        })
    }
}

export const authApi = new Auth()
