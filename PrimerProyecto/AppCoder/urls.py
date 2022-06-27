
from django.urls import path
from AppCoder.views import *

from . import views

urlpatterns = [
    path("DisiplinasDeportivas", views.disciplinasDeportivas),
    path("Profesores",views.profesores),
    path("Alumnos",views.alumnos),
    path("Sedes",views.sedes),
]