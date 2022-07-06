from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate

from Aplicaciones.AutosApp.models import Contacto
from .forms import ContactoForm
# Create your views here.

#DEF PAGINAS
def inicio(request):
    return render(request,"inicio.html",{})

def base(request):
    return render(request,"base.html",{})

def noticias(request):
    return render(request,"noticias.html",{})

def consejos(request):
    return render(request,"consejos.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def opiniones(request):
    return render(request,"opiniones.html",{})

def confirmacion(request):
    return render(request,"confirmacion.html",{})

#DEF PERFIL
def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
            
    form = AuthenticationForm()
                
    return render(request,"login.html",{"form":form})

def registrarse(request):
    
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            form.save()
            
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")           
            
        return render(request,"registrarse.html",{"form":form})
    
    form = UserCreationForm()
        
    return render(request,"registrarse.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")    

def editar_perfil(request,perfil_id):
    perfil = UserCreationForm.objects.get()
    

#DEF NOTICIAS
def noticia1(request):
    return render(request,"noticias/noticia1.html",{})

def noticia2(request):
    return render(request,"noticias/noticia2.html",{})

def noticia3(request):
    return render(request,"noticias/noticia3.html",{})

#DEF CONTACTO
def mensaje(request):
      
    if request.method =="POST":
        
        formulario = request.POST
        
        contacto = Contacto(nombre = formulario['txtNombre'],email = formulario['txtEmail'],mensaje = formulario['mensaje'])
        contacto.save()
        return redirect('confirmacion')