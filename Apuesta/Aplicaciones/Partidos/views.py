from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Equipo, Partido, Apuesta
from .serializers import EquipoSerializer, PartidoSerializer, ApuestaSerializer

# Create your views here.

def equipoApi(request):

    context={'equipo': Equipo.objects.all()}
    return render(request, "gestionApuestas.html",context)

"""def equipoApi(request,id=0):
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        equipos_serializer = EquipoSerializer(equipos,many=True)
        return JsonResponse(equipos_serializer.data,safe=False)
    elif request.method == 'POST':
        equipos_data=JSONParser().parse(request)
        equipos_serializer = EquipoSerializer(data=equipos_data)
        if equipos_serializer.isValid():
            equipos_serializer.save()
            return JsonResponse("Añadido con exito",safe=False)
        return JsonResponse("Fallo en añadir",safe=False) 
    elif request.method == "PUT":
        equipos_data=JSONParser().parse(request)
        equipos=Equipo.objects.get(pais=equipos_data['pais'])
        equipos_serializer=EquipoSerializer(equipos,data=equipos_data)
        if equipos_serializer.isValid():
            equipos_serializer.save()
            return JsonResponse("Actualizado con exito",safe=False)
        return JsonResponse("Fallo en actualizar",safe=False)
    elif request.method == 'DELETE':
        equipos=Equipo.objects.get(pais=id)
        equipos.delete()
        return JsonResponse("Eliminado con exito",safe=False)"""