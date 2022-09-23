# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Apps.productos.models import Producto, Comprar
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comprar)
admin.site.register(Producto, ClienteAdmin)
