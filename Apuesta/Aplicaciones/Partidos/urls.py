from django.urls import re_path
from . import views

urlpatterns = [
    re_path('',views.partido),
    #path('registrarApuesta/',views.registrarApuesta),
    #path('registrandoApuesta/<codigo>',views.registrandoApuesta),
]