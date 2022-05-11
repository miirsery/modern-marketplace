export const validatePassword = (
    password: string | number,
    retryPassword: string | number
): boolean => {
    return password === retryPassword
}