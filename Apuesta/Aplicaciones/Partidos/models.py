from django.db import models
#from djongo import models

# Create your models here.

class Equipo(models.Model):
    pais = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['grupo']

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.pais, self.grupo)

class Partido(models.Model):
    clasificacion = models.CharField(max_length=50)
    equipos1 = models.ForeignKey(Equipo,default=None,on_delete=models.PROTECT,related_name="_equipos1")
    equipos2 = models.ForeignKey(Equipo,default=None,on_delete=models.PROTECT,related_name="_equipos2")
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    fecha = models.DateField()

    def __str__(self):
        texto = "{0} ({1} {2})"
        return texto.format(self.clasificacion,self.equipos1,self.equipos2)

class Apuesta(models.Model):
    codigo_partido = models.ForeignKey(Partido,blank=True,null=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marcador1 = models.CharField(max_length=2)
    marcador2 = models.CharField(max_length=2)
    monto = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.monto)