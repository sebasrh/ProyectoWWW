from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^equipo$',views.equipoApi),
    re_path(r'^equipo/([0-9]+)$',views.equipoApi),
    #path('registrarApuesta/',views.registrarApuesta),
    #path('registrandoApuesta/<codigo>',views.registrandoApuesta),
]