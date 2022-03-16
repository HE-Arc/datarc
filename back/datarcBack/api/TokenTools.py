from api.models import User, File

def getUser(token):
    users = User.objects.all().filter(token=token)    
    if len(users) == 1:
        return users[0]
    return -1