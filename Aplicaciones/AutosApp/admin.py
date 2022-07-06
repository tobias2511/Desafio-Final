from django.contrib import admin
from .models import *
# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','mensaje')
    search_fields = ('nombre','email','mensaje')

admin.site.register(Contacto,ContactoAdmin)