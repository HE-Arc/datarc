function validPassword(password) {
    const re = /(?=.*?[a-z])(?=.*?[0-9]).{6,}/;
    let foundPassword = re.exec(password);
    return foundPassword == password;
}

function validUsername(username) {
    const re = /^[A-Za-z0-9]{2,24}/;
    let foundUsername = re.exec(username);
    return foundUsername == username;
    
}

export { validUsername, validPassword }