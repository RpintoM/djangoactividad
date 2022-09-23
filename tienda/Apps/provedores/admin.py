# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import imp
from django.contrib import admin
from Apps.provedores.models import Provedore, Distribuir

# Register your models here.


class MembershipInline(admin.TabularInline):
    model = Distribuir
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

class ProvedoreAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)



admin.site.register(Provedore, ProvedoreAdmin)
