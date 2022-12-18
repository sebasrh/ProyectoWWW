from django.contrib import admin
from .models import Partido, Equipo, Apuesta

admin.site.register(Apuesta)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id','pais','grupo')
    ordering = ['grupo']

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('id','equipos1','equipos2')
    ordering = ['clasificacion']