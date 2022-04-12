import re

def valid_user_name(name):
    pattern = r"^[A-Za-z0-9]{2,24}"
    p = re.compile(pattern)
    return bool(p.fullmatch(name))    
    
def valid_user_password(password):
    pattern = r"(?=.*?[a-z])(?=.*?[0-9]).{6,}"
    p = re.compile(pattern)
    return bool(p.fullmatch(password))

def valid_user_token(token):
    return True

def valid_file_name(name):
    return True

def valid_file_public(public):
    return True

def valid_file_url(url):
    return True
