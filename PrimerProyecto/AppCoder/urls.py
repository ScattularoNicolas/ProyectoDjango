
from django.urls import path
from AppCoder.views import *

from . import views

urlpatterns = [
    path("DisiplinasDeportivas", views.disciplinasDeportivas, name='disciplinasDeportivas'),
    path("Profesores", views.profesores, name='profesores'),
    path("Alumnos", views.alumnos, name='alumnos'),
    path("Sedes", views.sedes, name='sedes'),
]