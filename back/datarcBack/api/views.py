from importlib.metadata import requires
from django.shortcuts import render
from api.models import User, File, UserFile, UserAccess
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json
import uuid
from api.validator import *
from api.TokenTools import *
from django.core.files import File as djangoFile
from django.http import FileResponse


FILE_PATH = "/home/mat/Desktop/data"

def index(request):
    user = User(name="joe", password="mdp")
    user.save()
    return HttpResponse("API.")


#return user info if valid token
def user(request):
    print("salut")
    if request.method == 'GET':
        user = getUser(request)
        if user != -1:
            return JsonResponse({'status' : 'ok', 'name' : user.name})
        else:
            return JsonResponse({'status' : 'wrong token'})
    return JsonResponse({'status' : 'error wrong arguments'}) 

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
        except:
            return JsonResponse({'status' : 'error body'})
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
        try:
            data = json.loads(request.body) 
        except:
            return JsonResponse({'status' : 'error body'})
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

@csrf_exempt    
def file(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
        except:
            return JsonResponse({'status' : 'error body'})
        if 'name' and 'public' in data.keys():
            if valid_file_name(data['name']) and valid_file_public(data['public']):
                user = getUser(request)
                if user == -1:
                    return JsonResponse({'status' : 'error token'})
                
                public = data['public'] == "True"
                url = str(uuid.uuid4()).replace('-', '')
                new_file = File(name=data["name"], public=public, path=FILE_PATH+'/'+url, url=url)
                new_file.save()
                
                UserFile(userId=user.id, fileId=new_file.id).save()
                UserAccess(userId=user.id, fileId=new_file.id).save()
                
                return JsonResponse({'status' : 'ok', 'url' : url})
            
    elif request.method == 'GET':
        if 'url' in request.GET.keys():
            if valid_file_url(request.GET['url']):
                files =  File.objects.all().filter(url=request.GET['url'])
                if len(files) != 1:
                    return JsonResponse({'status' : 'error file doesnt exist'})
                my_file = files[0]
                if my_file.public == True:
                    return FileResponse( open(my_file.path, "rb"))
                else:
                    user = getUser(request)
                    if user == -1:
                        return JsonResponse({'status' : 'error wrong token'})
                    files_right = UserAccess.objects.all().filter(userId=user.id, fileId=my_file.id)
                    if len(files_right) != 1:
                        return JsonResponse({'status' : 'error file access'})
                    return FileResponse( open(my_file.path, "rb"))
  
                    
    return JsonResponse({'status' : 'error'})
    
    
    
def files(request):
    user = getUser(request)
    if user == -1:
        return JsonResponse({'status' : 'error user doesnt exist'})    
    user_access = UserAccess.objects.all().filter(userId=user.id)
    files_id = map(lambda elem : elem.fileId, user_access)
    files = []
    for id in files_id:
        files.append(File.objects.all().filter(id=id)[0])              
    result = {"status" : "ok", "files" : len(files)}
    return JsonResponse(result)


@csrf_exempt    
def upload(request):
    data = request.body
    try:
        data = request.body
    except:
        return JsonResponse({'status' : 'error body file too big'})
    
    if request.method == 'POST': 
        if not 'url' in list(request.GET.keys()):
            return JsonResponse({'status' : "error query params"})
        if not valid_file_url(request.GET.get('url')):
            return JsonResponse({'status' : "error url"}) 
        dbfiles = File.objects.all().filter(url=request.GET.get('url'))
        if not len(dbfiles) == 1:
            return JsonResponse({'status' : "error file"})
        
        f = open(dbfiles[0].path, "wb")
        myfile = djangoFile(f)
        f.write(data)
        myfile.close()
        f.close()
        return JsonResponse({'status' : 'file uploaded'})
        

    return JsonResponse({'status' : 'error wrong method'})