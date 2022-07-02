from django.shortcuts import render

# Create your views here.
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

