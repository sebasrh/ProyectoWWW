from django.db import models
#from djongo import models

# Create your models here.

class Equipo(models.Model):
    pais = models.CharField(primary_key=True,max_length=50)
    grupo = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.pais, self.grupo)


class Partido(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    equipos = models.ForeignKey(Equipo,blank=True,null=True,on_delete=models.CASCADE)
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    fecha = models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)

class Apuesta(models.Model):
    codigo_apuesta = models.CharField(primary_key=True,max_length=6)
    codigo_partido = models.ForeignKey(Partido,blank=True,null=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    monto = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)