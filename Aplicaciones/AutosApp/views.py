from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from Aplicaciones.AutosApp.forms import UserEditForm
from Aplicaciones.AutosApp.models import Contacto, Opinion

# Create your views here.

#DEF PAGINAS
def inicio(request):
    return render(request,"inicio.html",{})

def base(request):
    return render(request,"base.html",{})

def noticias(request):
    return render(request,"noticias.html",{})

def consejos2(request):
    return render(request,"consejos2.html",{})

def consejos(request):
    return render(request,"consejos.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def confirmacion(request):
    return render(request,"confirmacion.html",{})

def creador(request):
    return render(request,"creador.html",{})

def opiniones(request):
    opinion= Opinion.objects.all()
    return render(request,"opiniones.html",{"opinion":opinion})

def agregarOpinion(request):
    
    if request.method == "POST":
        
        info_formulario = request.POST
        
        opinion = Opinion(nombre = info_formulario['txtNombre'],apellido = info_formulario['txtApellido'],mensaje = info_formulario['txtMensaje'])
        opinion.save()
        return redirect('opiniones')


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

@login_required
def editar_perfil(request):
    
    user = request.user 

    if request.method == "POST":
        
        form = UserEditForm(request.POST) 

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            #user.password = info["password1"]
                        
            user.save()

            return redirect("inicio")


    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"editar_perfil.html",{"form":form})
    
    

#DEF NOTICIAS
def noticia1(request):
    return render(request,"noticias/noticia1.html",{})

def noticia2(request):
    return render(request,"noticias/noticia2.html",{})

def noticia3(request):
    return render(request,"noticias/noticia3.html",{})

def noticia4(request):
    return render(request,"noticias/noticia4.html",{})

#DEF CONSEJOS
def consejo1(request):
    return render(request,"consejos/consejo1.html",{})

def consejo2(request):
    return render(request,"consejos/consejo2.html",{})

def consejo3(request):
    return render(request,"consejos/consejo3.html",{})

def consejo4(request):
    return render(request,"consejos/consejo4.html",{})

#DEF CONTACTO
def mensaje(request):
      
    if request.method =="POST":
        
        formulario = request.POST
        
        contacto = Contacto(nombre = formulario['txtNombre'],email = formulario['txtEmail'],mensaje = formulario['mensaje'])
        contacto.save()
        return redirect('confirmacion')