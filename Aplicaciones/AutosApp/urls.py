from django.urls import path
from .views import *
urlpatterns = [
    
    #URLS PAGINAS
    path('',inicio,name="inicio"),    
    path('base/',base,name="base"),
    path('contacto/',contacto,name="contacto"),
    path('consejos/',consejos,name="consejos"),
    path('consejos2/',consejos2,name="consejos2"),
    path('noticias/',noticias,name="noticias"),
    path('opiniones/',opiniones,name="opiniones"),
    path('mensaje/',mensaje,name = "mensaje"),
    path('confirmacion/',confirmacion,name = "confirmacion"),
    path('editar_perfil/',editar_perfil,name = "editar_perfil"),
    path('creador/',creador,name = "creador"),
    path('agregarOpinion/',agregarOpinion),

       
    #URLS PERFIL
    path('login/',login_request,name="login"),
    path('registrarse/',registrarse,name="registrarse"),
    path('logout/',logout_request,name="logout"),
    
    # URLS NOTICIAS
    path('noticia1/',noticia1,name="noticia1"),
    path('noticia2/',noticia2,name="noticia2"),
    path('noticia3/',noticia3,name="noticia3"),
    path('noticia4/',noticia4,name="noticia4"),
    
    # URLS CONSEJOS
    path('consejo1/',consejo1,name="consejo1"),
    path('consejo2/',consejo2,name="consejo2"),
    path('consejo3/',consejo3,name="consejo3"),
    path('consejo4/',consejo4,name="consejo4"),
     
]   
