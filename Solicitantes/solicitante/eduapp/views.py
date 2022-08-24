from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Apolinario Nathaly
#Barcia Karol
#Basurto Laura
#Bellolio Karla
#Montes Kelly
#Pilozo Noelia
#Pincay Mell

from django.template import loader

from docente.models import Docente


def bienvenidos(request):
    cantidad = Docente.objects.count()
    #docente = Docente.objects.all().values()
    docente = Docente.objects.order_by('apellido')
    mensaje = {'cantidad':cantidad,'docente':docente}
    pagina = loader.get_template('bienvenidos.html')
    return HttpResponse(pagina.render(mensaje, request))
