from pyexpat import model
from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField()

class Opinion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,blank=True,null=True)
    mensaje = models.TextField()

    