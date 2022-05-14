export type SignUpType = {
    email: string | number,
    username: string | number,
    password: string | number,
    retryPassword: string | number
}

export type ProfileUserType = {
    avatar: string,
    id: number,
    username: string,
}

export type ResetPasswordType = {
    email: string
}