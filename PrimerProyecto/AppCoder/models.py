from django.db import models

class DisiplinasDeportivas(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField("Precio $")

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)

class Sedes(models.Model):
    localidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=20)
    dia_y_horario = models.CharField(max_length=50)
    