#Grupo 5
#Apolinario Nathaly
#Barcia Karol
#Basurto Laura
#Bellolio Karla
#Montes Kelly
#Pilozo Noelia
#Pincay Mell
from rest_framework import serializers

from docente.models import Docente, Direccion, Telefono


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ['id', 'url', 'nombre', 'apellido', 'email', 'direccion']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'url', 'calle', 'no_calle', 'pais']

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ['id', 'url', 'telefono', 'tipo']
