export const getCookie = (name): any => {
    if (!document.cookie) return
    const matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));

    if (!matches) return

    return matches
}
