from django.urls import path
from . import views

urlpatterns = [
    path('',views.grupos),
    path('octavos/',views.octavos),
    path('cuartos/',views.cuartos),
    path('semis/',views.semis),
    path('finales/',views.finales),
    #path('registrarApuesta/',views.registrarApuesta),
    path('registrarApuesta/<id>',views.registrarApuesta),
]