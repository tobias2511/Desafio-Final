from distutils.command.upload import upload
from pyexpat import model
from tokenize import Triple
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()   

class Opinion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,blank=True,null=True)
    mensaje = models.TextField()
    
    
class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/',blank=True, null=Triple)