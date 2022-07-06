
from django.urls import path, include
from AppCoder.views import *
from django.contrib import admin

from . import views

urlpatterns = [
    
    path("disciplinasDeportivas/", views.disciplinasDeportivas, name='disciplinasDeportivas'),
    path("Profesores/", views.profesores, name='profesores'),
    path("Alumnos/", views.alumnos, name='alumnos'),
    path("Sedes/", views.sedes, name='sedes'),
    #path('inscripcion_deporte/', name='inscripcion'),
    #path("base/", base),
    
]