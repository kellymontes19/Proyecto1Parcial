"""solicitante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Apolinario Nathaly
#Barcia Karol
#Basurto Laura
#Bellolio Karla
#Montes Kelly
#Pilozo Noelia
#Pincay Mell
from rest_framework import routers

from docente import views
from docente.views import detalle_docente, nuevo_docente, modificar_docente, eliminar_docente, reporte_docente
from eduapp.views import bienvenidos

router = routers.DefaultRouter()
router.register(r'docentes', views.DocenteViewSet)
router.register(r'direciones', views.DireccionViewSet)
router.register(r'telefonos', views.TelefonoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name='inicio'),
    path('detalle_docente/<int:id>', detalle_docente, name='detalle_docente'),
    path('nuevo_docente/', nuevo_docente, name='nuevo_docente'),
    path('eliminar_docente/<int:id>', eliminar_docente, name='eliminar_docente'),
    path('reporte_docente/', reporte_docente, name='reporte_docente'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
