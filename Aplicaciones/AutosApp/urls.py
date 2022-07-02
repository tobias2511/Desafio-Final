from django.urls import path
from .views import *
urlpatterns = [
    path('',inicio,name="inicio"),
    
    path('base/',base,name="base"),
    path('contacto/',contacto,name="contacto"),
    path('consejos/',consejos,name="consejos"),
    path('noticias/',noticias,name="noticias"),
    path('opiniones/',opiniones,name="opiniones"),
  
]
