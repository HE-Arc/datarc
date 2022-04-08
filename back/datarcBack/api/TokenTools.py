from api.models import User, File

def getUserFromToken(token):
    users = User.objects.all().filter(token=token)    
    if len(users) == 1:
        return users[0]
    return -1


def getUser(request):
    try:
        token = request.headers.get('Authentication')
    except:
        return -1
    
    return getUserFromToken(token)