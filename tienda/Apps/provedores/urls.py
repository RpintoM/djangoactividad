from django.urls import path
from Apps.provedores.views import home

urlpatterns = [
 path('inicio/', home, name= 'home'),
]