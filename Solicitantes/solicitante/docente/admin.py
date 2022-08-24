from django.contrib import admin

# Register your models here.
from docente.models import Docente, Telefono, Direccion

admin.site.register(Docente)
admin.site.register(Telefono)
admin.site.register(Direccion)