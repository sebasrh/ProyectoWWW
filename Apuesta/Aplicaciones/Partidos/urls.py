from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('grupos/',views.grupos),
    path('octavos/',views.octavos),
    path('cuartos/',views.cuartos),
    path('semis/',views.semis),
    path('finales/',views.finales),
    path('registrarApuesta/<id>',views.registrarApuesta),
    path('octavos/registrarApuesta/<id>',views.registrarApuesta),
    path('cuartos/registrarApuesta/<id>',views.registrarApuesta),
    path('semis/registrarApuesta/<id>',views.registrarApuesta),
    path('finales/registrarApuesta/<id>',views.registrarApuesta),
    path('hacerApuesta/<id>',views.hacerApuesta),
    path('octavos/hacerApuesta/<id>',views.hacerApuesta),
    path('cuartos/hacerApuesta/<id>',views.hacerApuesta),
    path('semis/hacerApuesta/<id>',views.hacerApuesta),
    path('finales/hacerApuesta/<id>',views.hacerApuesta),
    path('resultados/',views.resultados),
]