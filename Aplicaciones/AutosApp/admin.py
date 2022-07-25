from django.contrib import admin
from .models import *
# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','mensaje')
    search_fields = ('nombre','email','mensaje')
    
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','mensaje')
    search_fields = ('nombre','apellido','mensaje')

admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Opinion,OpinionAdmin)
admin.site.register(Avatar)
