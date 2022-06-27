from django.contrib import admin

from .models import Alumnos, DisiplinasDeportivas, Profesores, Sedes

class DisiplinasDeportivasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    
admin.site.register(DisiplinasDeportivas, DisiplinasDeportivasAdmin)

class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "deporte")
    
admin.site.register(Profesores, ProfesoresAdmin)

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "deporte")
    
admin.site.register(Alumnos, AlumnosAdmin)

class SedesAdmin(admin.ModelAdmin):
    list_display = ("localidad", "direccion", "provincia", "dia_y_horario")
    
admin.site.register(Sedes, SedesAdmin)