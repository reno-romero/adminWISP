from django.db import models

# Create your models here.

class Equipo(models.Model):
    marca = models.CharField(max_length=35)    
    modelo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return '%s %s' %(self.modelo, self.marca)

class Paquete(models.Model):
    velocidad = models.IntegerField()
    costo = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return '%s' % self.velocidad


class Sitio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)
    info_contacto = models.TextField()
    notas = models.TextField()

    def __str__(self):
        return '%s' % self.nombre

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    tipo_cliente = models.CharField(max_length=20)
    notas = models.TextField()
    domicilio = models.CharField(max_length=30)
    ciudad_municipio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=100)
    cp = models.IntegerField()
    facturacion = models.NullBooleanField()
    telefono = models.DecimalField(max_digits=12, decimal_places=0)
    me_dirijo_con = models.CharField(max_length=30)
    mail = models.CharField(max_length=70)
    whatsapp = models.DecimalField(max_digits=12, decimal_places=0)
    paquete_internet = models.ForeignKey(Paquete,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    mastil = models.IntegerField()
    modem = models.CharField(max_length=15)
    fecha_pago = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' %(self.id, self.nombre, self.apellidos)



class DatosInstalacione(models.Model):
    nombre_cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    ip_asignada = models.CharField(max_length=15)
    conectado_a = models.ForeignKey(Sitio,on_delete=models.CASCADE)
    fecha_instalacion = models.DateTimeField(auto_now=True)
    siguiente_pago = models.CharField(max_length=30)
    antena = models.CharField(max_length=15)
    mastil = models.IntegerField()
    plan = models.CharField(max_length=25)

    def __str__(self):
        return '%s' % self.nombre_cliente

class Pago(models.Model):
    cliente = models.ForeignKey(DatosInstalacione,on_delete=models.CASCADE)    
    dias_pago = models.CharField(max_length=2)
    mes_pagado = models.CharField(max_length=12)
    pagado = models.NullBooleanField(null=True)

    def __str__(self):
        return '%s %s' %(self.cliente, self.estatus)

