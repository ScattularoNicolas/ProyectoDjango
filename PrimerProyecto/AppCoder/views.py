from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import NuevoDeporte

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
        disciplinasDeportivas = DisiplinasDeportivas(nombre = info_formulario["nombre"], precio = int (info_formulario["precio"]))
        disciplinasDeportivas.save()
        
        return render(request, "AppCoder/inscripcion_deporte.html", {} )
    #Método GET
    else:
        formularioVacio = NuevoDeporte()
        return render(request, "AppCoder/inscripcion_deporte.html", {"form":formularioVacio} )
    
