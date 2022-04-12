from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    token = models.CharField(max_length=50)


class File(models.Model):
    name = models.CharField(max_length=50)
    public = models.BooleanField()
    path = models.CharField(max_length=100)
    url = models.CharField(max_length=50)

    
class UserFile(models.Model):
    userId = models.IntegerField()
    fileId = models.IntegerField()
    
class UserAccess(models.Model):
    userId = models.IntegerField()
    fileId = models.IntegerField()
