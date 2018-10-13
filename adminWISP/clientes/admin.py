from django.contrib import admin
from .models import Clientes, DatosInstalacione, Equipo, Paquete, Sitio, Pago

# Register your models here.

admin.site.register(Clientes)
admin.site.register(DatosInstalacione)
admin.site.register(Equipo)
admin.site.register(Paquete)
admin.site.register(Sitio)
admin.site.register(Pago)