from django.contrib import admin
from .models import Partido, Equipo, Apuesta

@admin.register(Apuesta)
class ApuestaAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_partido','nombre','marcador1','marcador2','monto')
    ordering = ['codigo_partido']

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id','pais','grupo')
    ordering = ['grupo']

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('id','clasificacion','equipos1','equipos2','marcador1','marcador2','fecha')
    ordering = ['clasificacion']