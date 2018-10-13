"""adminWISP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from clientes import views 
from clientes.views import Alta_Usuario, ClientesLista

urlpatterns = [
    path('login/', admin.site.urls),
    path('', views.inicio),
    path('<slug:slug>/<int:pk>', ClientesLista.as_view(),name="clientes"),
    path('inicio/', views.inicio),
    path('servicios/', views.servicios),
    path('contacto/', views.contacto),
    path('nuevo/', Alta_Usuario.as_view(),name="nuevo"),
]
