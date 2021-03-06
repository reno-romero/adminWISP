# Generated by Django 2.0.2 on 2018-10-01 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=40)),
                ('tipo_cliente', models.CharField(max_length=20)),
                ('notas', models.TextField()),
                ('domicilio', models.CharField(max_length=30)),
                ('ciudad_municipio', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=100)),
                ('cp', models.IntegerField()),
                ('facturación', models.BooleanField()),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=12)),
                ('me_dirijo_con', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=70)),
                ('whatsapp', models.DecimalField(decimal_places=0, max_digits=12)),
                ('mastil', models.IntegerField()),
                ('modem', models.CharField(max_length=15)),
                ('fecha_pago', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatosInstalacione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_asignada', models.CharField(max_length=15)),
                ('fecha_instalacion', models.DateTimeField(auto_now=True)),
                ('siguiente_pago', models.CharField(max_length=30)),
                ('antena', models.CharField(max_length=15)),
                ('mastil', models.IntegerField()),
                ('plan', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=35)),
                ('modelo', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_pago', models.CharField(max_length=2)),
                ('mes_pagado', models.CharField(max_length=12)),
                ('estatus', models.BooleanField(verbose_name=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.DatosInstalacione')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velocidad', models.IntegerField()),
                ('costo', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40)),
                ('info_contacto', models.TextField()),
                ('notas', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='datosinstalacione',
            name='conectado_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Sitio'),
        ),
        migrations.AddField(
            model_name='datosinstalacione',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Equipo'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='paquete_internet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Paquete'),
        ),
    ]
