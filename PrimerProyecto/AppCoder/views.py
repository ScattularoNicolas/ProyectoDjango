from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

#def index(request):
    #return HttpResponse("Funciona")

def disciplinasDeportivas(request):
    deportes = DisiplinasDeportivas.objects.all()
    return render(request, "AppCoder/disciplinas_deportivas.html", {"deportes": deportes})

def profesores (request):
    profesor = Profesores.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesor": profesor})

def alumnos (request):
    alumno = Alumnos.objects.all()
    return render(request, "AppCoder/alumnos.html", {"alumno":alumno})

def sedes (request):
    sede = Sedes.objects.all()
    return render(request, "AppCoder/sedes.html", {"sede":sede})

def base(request):
    
    return render(request, "AppCoder/base.html, {}")
    
def inscripcion_deporte(request):
    
    if request.method == "POST":
        info_formulario = request.POST
        disciplinasDeportivas = DisiplinasDeportivas(request.POST["nombre"], request.POST["precio"])
        disciplinasDeportivas.save()
        
        return render(request, "AppCoder/inscripcion_deporte.html", {} )
    
    else:
        return render(request, "AppCoder/inscripcion_deporte.html", {} )
    
