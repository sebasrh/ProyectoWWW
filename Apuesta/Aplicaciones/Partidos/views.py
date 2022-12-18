from django.shortcuts import render, redirect
from .models import Equipo, Partido, Apuesta

# Create your views here.

def grupos(request):
    context={'partido': Partido.objects.filter(clasificacion='grupos')}
    return render(request, "gestionApuestasGrupos.html",context)

def octavos(request):
    context={'partido': Partido.objects.filter(clasificacion='octavos')}
    return render(request, "gestionApuestasOctavos.html",context)

def cuartos(request):
    context={'partido': Partido.objects.filter(clasificacion='cuartos')}
    return render(request, "gestionApuestasCuartos.html",context)

def semis(request):
    context={'partido': Partido.objects.filter(clasificacion='semifinales')}
    return render(request, "gestionApuestasSemis.html",context)

def finales(request):
    context={'partido': Partido.objects.filter(clasificacion='final')}
    return render(request, "gestionApuestasFinales.html",context)

def registrarApuesta(request,id):
    context={'partido':Partido.objects.get(id=id)}
    return render(request,"registrarApuesta.html",context)