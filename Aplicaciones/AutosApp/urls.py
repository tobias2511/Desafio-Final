from django.urls import path
from .views import *
urlpatterns = [
    
    #URLS PAGINAS
    path('',inicio,name="inicio"),    
    path('base/',base,name="base"),
    path('contacto/',contacto,name="contacto"),
    path('consejos/',consejos,name="consejos"),
    path('consejos2/',consejos2,name="consejos2"),
    path('consejos3/',consejos3,name="consejos3"),
    path('noticias/',noticias,name="noticias"),
    path('noticias2/',noticias2,name="noticias2"),
    path('noticias3/',noticias3,name="noticias3"),
    path('opiniones/',opiniones,name="opiniones"),
    path('creador/',creador,name = "creador"),
    path('mensaje/',mensaje,name = "mensaje"),
    path('confirmacion/',confirmacion,name = "confirmacion"),
    path('editar_perfil/',editar_perfil,name = "editar_perfil"),
    path('editar_comentario/',editar_comentario,name = "editar_comentario"),
    path('agregarOpinion/',agregarOpinion),
    path('agregar_avatar',agregar_avatar,name = "agregar_avatar"),

       
    #URLS PERFIL
    path('login/',login_request,name="login"),
    path('registrarse/',registrarse,name="registrarse"),
    path('logout/',logout_request,name="logout"),
    
    # URLS NOTICIAS
    path('noticia1/',noticia1,name="noticia1"),
    path('noticia2/',noticia2,name="noticia2"),
    path('noticia3/',noticia3,name="noticia3"),
    path('noticia4/',noticia4,name="noticia4"),
    path('noticia5/',noticia5,name="noticia5"),
    path('noticia6/',noticia6,name="noticia6"),
    path('noticia7/',noticia7,name="noticia7"),
    path('noticia8/',noticia8,name="noticia8"),
    path('noticia9/',noticia9,name="noticia9"),
    path('noticia10/',noticia10,name="noticia10"),
    path('noticia11/',noticia11,name="noticia11"),
    path('noticia12/',noticia12,name="noticia12"),
    
    # URLS CONSEJOS
    path('consejo1/',consejo1,name="consejo1"),
    path('consejo2/',consejo2,name="consejo2"),
    path('consejo3/',consejo3,name="consejo3"),
    path('consejo4/',consejo4,name="consejo4"),
    path('consejo5/',consejo5,name="consejo5"),
    path('consejo6/',consejo6,name="consejo6"),
    path('consejo7/',consejo7,name="consejo7"),
    path('consejo8/',consejo8,name="consejo8"),
    path('consejo9/',consejo9,name="consejo9"),
    path('consejo10/',consejo10,name="consejo10"),
    path('consejo11/',consejo11,name="consejo11"),
    path('consejo12/',consejo12,name="consejo12"),
     
]   
