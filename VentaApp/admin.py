from django.contrib import admin
from VentaApp.models import Cliente

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display= ("nombres", "apellidos", "direccion", "telefono")

admin.site.register(Cliente, ClientesAdmin)
