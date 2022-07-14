from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from Aplicaciones.AutosApp.forms import UserEditForm,UserRegisterForm
from Aplicaciones.AutosApp.models import Contacto, Opinion

# Create your views here.

#DEF PAGINAS
def inicio(request):
    return render(request,"inicio.html",{})

def base(request):
    return render(request,"base.html",{})

def noticias(request):
    return render(request,"noticias.html",{})

def noticias2(request):
    return render(request,"noticias2.html",{})

def noticias3(request):
    return render(request,"noticias3.html",{})

def consejos(request):
    return render(request,"consejos.html",{})

def consejos2(request):
    return render(request,"consejos2.html",{})

def consejos3(request):
    return render(request,"consejos3.html",{})

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
        
        opinion = Opinion(nombre = info_formulario['txtNombre'],apellido = info_formulario['txtApellido'],mensaje = info_formulario['txtMensaje'],valoraciones = info_formulario['txtValoracion'])
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
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            form.save()
            
            user = authenticate(username=username,password1=password1,password2=password2,email=email,first_name=first_name,last_name=last_name)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")           
            
        return render(request,"registrarse.html",{"form":form})
    
    form = UserRegisterForm()
        
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
            user.password1 = info["password1"]
            user.password2 = info["password2"]  
                        
            user.save()

            return redirect("inicio")


    else:
        form = UserEditForm(initial={"email":user.email})

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

def noticia5(request):
    return render(request,"noticias/noticia5.html",{})

def noticia6(request):
    return render(request,"noticias/noticia6.html",{})

def noticia7(request):
    return render(request,"noticias/noticia7.html",{})

def noticia8(request):
    return render(request,"noticias/noticia8.html",{})

#DEF CONSEJOS
def consejo1(request):
    return render(request,"consejos/consejo1.html",{})

def consejo2(request):
    return render(request,"consejos/consejo2.html",{})

def consejo3(request):
    return render(request,"consejos/consejo3.html",{})

def consejo4(request):
    return render(request,"consejos/consejo4.html",{})

def consejo5(request):
    return render(request,"consejos/consejo5.html",{})

def consejo6(request):
    return render(request,"consejos/consejo6.html",{})

def consejo7(request):
    return render(request,"consejos/consejo7.html",{})

def consejo8(request):
    return render(request,"consejos/consejo8.html",{})

def consejo9(request):
    return render(request,"consejos/consejo9.html",{})

def consejo10(request):
    return render(request,"consejos/consejo10.html",{})

def consejo11(request):
    return render(request,"consejos/consejo11.html",{})

def consejo12(request):
    return render(request,"consejos/consejo12.html",{})



#DEF CONTACTO
def mensaje(request):
      
    if request.method =="POST":
        
        formulario = request.POST
        
        contacto = Contacto(nombre = formulario['txtNombre'],email = formulario['txtEmail'],mensaje = formulario['mensaje'])
        contacto.save()
        return redirect('confirmacion')