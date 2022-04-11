from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('file/', views.file, name='file'),
    path('files/', views.files, name='files'),
    path('upload/', views.upload, name='upload'),
    path('user/', views.user, name='user'),

]