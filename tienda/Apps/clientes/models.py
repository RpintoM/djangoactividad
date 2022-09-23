# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100, help_text="Ingrese el Nombre del Cliente")
    apellidosCliente = models.CharField(max_length=100, help_text="Ingrese el Apellido del Cliente")
    direccionCliente = models.CharField(max_length=100, help_text="Ingrese la Direccion del Cliente")
    telefonoCliente = models.CharField(max_length=12, help_text="Ingrese el Telefono del Cliente")
   

    def __str__(self):
        return self.nombreCliente

    #class Meta:
        #verbose_name = "cliente"
        #verbose_name_plural = "clientes"
