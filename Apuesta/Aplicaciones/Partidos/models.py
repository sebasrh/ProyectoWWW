from django.db import models
#from djongo import models

# Create your models here.

class Equipo(models.Model):
    pais = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.pais, self.grupo)

class Partido(models.Model):
    clasificacion = models.CharField(max_length=50)
    equipos1 = models.ForeignKey(Equipo,blank=False,null=False,on_delete=models.CASCADE,related_name="_equipos1")
    equipos2 = models.ForeignKey(Equipo,blank=False,null=False,on_delete=models.CASCADE,related_name="_equipos2")
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    fecha = models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.clasificacion, self.codigo)

class Apuesta(models.Model):
    codigo_partido = models.ForeignKey(Partido,blank=True,null=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    monto = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.monto)