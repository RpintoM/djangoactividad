# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Apps.productos.models import Producto

# Create your models here.


class Provedore(models.Model):
    nombreProvedor = models.CharField(max_length=100, help_text="Ingrese el Nombre del Provedor")
    apellidoProvedor = models.CharField(max_length=100, help_text="Ingrese el Apellido del Provedor")
    direccionProvedor = models.CharField(max_length=100, help_text="Ingrese la Direccion del Provedor")
    provinciaProvedor = models.CharField(max_length=100, help_text="Ingrese la Provincia del Provedor")
    telefonoProvedor = models.CharField(max_length=12, help_text="Ingrese el Telefono del Provedor")
    

    def __str__(self):
        return self.nombreProvedor

    class Meta:
        verbose_name = "provedore"
        verbose_name_plural = "provedores"



class Distribuir(models.Model):
    cantidadProductos = models.CharField(max_length=50, verbose_name="Cantidad Productos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    provedore = models.ForeignKey(Provedore, on_delete=models.CASCADE, verbose_name="Provedore")

    def __str__(self):
        return self.cantidadProductos


       
