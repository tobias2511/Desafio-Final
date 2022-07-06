from django import forms
from .models import Contacto
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

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}