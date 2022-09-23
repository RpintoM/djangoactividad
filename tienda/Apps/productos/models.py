# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Apps.clientes.models import Cliente
from django.db import models

#from clases.tienda.Apps.provedores.models import Provedore
# Create your models here.


class Producto(models.Model):
    descricion = models.CharField(max_length=50, verbose_name="Describir producto")
    precio = models.FloatField(verbose_name="Precio")
    numeroExistencia = models.IntegerField(verbose_name="Cantidad")
    #producto = models.ForeignKey(Producto,
                                    #null=True,
                                    #blank=True,
                                    #on_delete=models.CASCADE)

    def __str__(self):
        return self.descricion

    #class Meta:
      #verbose_name = "producto"
      #Sverbose_name_plural = " productos"
      
class Comprar(models.Model):
    fechaCompra = models.DateTimeField(auto_now=True, verbose_name="Fecha de Compra")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")

    #def __str__(self):
        #return self.nombre

    #class Meta:
        #verbose_name = "distribuir"
       
