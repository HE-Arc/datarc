function validPassword(password) {
    const re = /(?=.*?[a-z])(?=.*?[0-9]).{6,}/;
    return re.test(password);
}

// todo rename into Username
function validMail(mail) {
    const re = /^[A-Za-z0-9]{2,24}/;
    return re.test(mail);
}

export { validMail, validPassword }