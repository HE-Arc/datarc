function validPassword(password) {
    const re = /(?=.*?[a-z])(?=.*?[0-9]).{6,}/;
    return re.test(password);
}

function validMail(mail) {
    const re = /[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+/;
    return re.test(mail);
}

export { validMail, validPassword }