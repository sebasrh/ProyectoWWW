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

def hacerApuesta(request,id):
    nombre = request.POST['txtNombre']
    marcador1 = request.POST['txtMarcador1']
    marcador2 = request.POST['txtMarcador2']
    monto = request.POST['txtMonto']

    codigo_partido=Partido.objects.get(id=id)

    apuesta=Apuesta.objects.create(codigo_partido=codigo_partido,nombre=nombre, marcador1=marcador1, marcador2=marcador2, monto=monto)
    
    return redirect('/resultados/')

def resultados(request):
    context={'apuesta':Apuesta.objects.all()}
    return render(request,"gestionApuestasResultados.html",context)