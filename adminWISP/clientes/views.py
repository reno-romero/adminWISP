
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes, DatosInstalacione

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def hello_world(request):
    return HttpResponse("hola mundo cruel!!!!")

#def clientes(request):
#   clientes = Clientes.objects.all()
#  instalaciones = DatosInstalacione.objects.all()

    return render(request, 'clientes_list.html', {"clientes":clientes, "instalaciones":instalaciones})

def inicio(request):
    return render(request, 'inicio.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

class ClientesLista(DetailView):
    model = Clientes


class Alta_Usuario(CreateView):
    model = Clientes
    fields = ['nombre', 'apellidos', 'tipo_cliente', 'notas', 'domicilio', 'ciudad_municipio', 'localidad', 'cp', 'facturacion', 'telefono', 'me_dirijo_con', 'mail', 'whatsapp', 'paquete_internet', 'equipo', 'mastil', 'modem']    
    
