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
        formulario = NuevoDeporte(request.POST)
        
        if formulario.is_valid():
            info_deporte = formulario.cleaned_data
            disciplinasDeportivas = DisiplinasDeportivas(nombre = info_deporte["nombre"], precio = int (info_deporte["precio"]))
            disciplinasDeportivas.save()
            return redirect("disciplinas_deportivas")
        else:
            redirect("disciplinas_deportivas")
    #Método GET
    else:
        formularioVacio = NuevoDeporte()
        return render(request, "AppCoder/inscripcion_deporte.html", {"form":formularioVacio} )
    
