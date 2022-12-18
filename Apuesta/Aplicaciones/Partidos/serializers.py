from rest_framework import serializers
from .models import Equipo, Partido, Apuesta

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipo
        fields=('pais','grupo')
    
class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Partido
        fields=('codigo','equipos','marcador1','marcador2','fecha')

class ApuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apuesta
        fields=('codigo_apuesta','codigo_partido', 'nombre','marcador1','marcador2','monto')