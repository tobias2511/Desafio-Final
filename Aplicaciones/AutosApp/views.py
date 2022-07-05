from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
# Create your views here.
def inicio(request):
    return render(request,"inicio.html",{})

def base(request):
    return render(request,"base.html",{})

def noticias(request):
    return render(request,"noticias.html",{})

def noticia1(request):
    return render(request,"noticias/noticia1.html",{})

def consejos(request):
    return render(request,"consejos.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

def opiniones(request):
    return render(request,"opiniones.html",{})

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect("login")
            
    form = AuthenticationForm()
                
    return render(request,"login.html",{"form":form})