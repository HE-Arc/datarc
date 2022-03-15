from django.shortcuts import render
from api.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json
import uuid
from api.validator import *

def index(request):
    user = User(name="joe", password="mdp")
    user.save()
    return HttpResponse("API.")

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if "name" and "password" in data.keys():
            if valid_user_name(data["name"]) and valid_user_password(data["password"]):    
                users = User.objects.all().filter(name=data["name"])
                if(len(users) > 0):
                    return JsonResponse({'status' : 'error user already exist'}) 
                mytoken = str(uuid.uuid4())
                new_user = User(name=data["name"], password=make_password(data["password"]), token=mytoken)
                new_user.save()
            return JsonResponse({'status' : 'ok', 'token' : mytoken}) 
        else:
            return JsonResponse({'status' : 'error wrong arguments'})
            
    return JsonResponse({'status' : 'error'})
    
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'name' and 'password' in data.keys():
                if valid_user_name(data["name"]) and valid_user_password(data["password"]):
                    users = User.objects.all().filter(name=data["name"])
                    if(len(users) > 0):
                        if check_password(data['password'], users[0].password):
                            return JsonResponse({'status' : 'ok', 'token' : users[0].token})
                        else:
                            return JsonResponse({'status' : 'error wrong password'})    
                    else:
                        return JsonResponse({'status' : 'error user doesnt exist'})
    return JsonResponse({'status' : 'error'})

    