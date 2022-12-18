from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Equipo, Partido, Apuesta

# Create your views here.

def partido(request):

    context={'partido': Partido.objects.all()}
    return render(request, "gestionApuestas.html",context)