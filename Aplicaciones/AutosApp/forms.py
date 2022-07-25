from django import forms
from .models import Contacto,Opinion,Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',]
        help_texts = {k:"" for k in fields}
        
class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    username = forms.CharField(label="Usuario")
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']

class OpinionForm(forms.Form):
    nombre = forms.CharField(label="nombre")
    apellido = forms.CharField(label="apellido")
    mensaje = forms.CharField(label="mensaje")
    
    class Meta:
        model = Opinion
        fields = ['nombre','apellido','mensaje']
        

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']