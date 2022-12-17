from django.db import models
#from djongo import models


# Create your models here.

class Equipo(models.Model):
    pais = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.pais, self.grupo)


"""class Partidos(models.Model):
    codigo = models.AutoField(primary_key=True)
    equipoA = models.CharField(max_length=50)
    equipoB = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)"""

"""class Apuesta(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.CharField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)"""