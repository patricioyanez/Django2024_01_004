from django.shortcuts import render
from .models import Alumno,Escuela,Carrera
# Create your views here.
def menu(request):
    context = {}
    return render(request, 'plantillaBase.html', context)
def index(request):
    context = {}
    return render(request, 'index.html', context)

def listarAlumnos(request):
    # utilizar ORM de Django
    # select * from alumno
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'listarAlumno.html', context)


def listarEscuela(request):
    # utilizar ORM de Django
    # select * from alumno
    listado = Escuela.objects.all()
    context = {'listado': listado}
    return render(request, 'listarEscuela.html', context)

def listarCarrera(request):
    # utilizar ORM de Django
    # select * from alumno
    listado = Carrera.objects.all()
    context = {'listado': listado}
    return render(request, 'listarCarrera.html', context)

def guardarCarrera(request):
    escuelas = Escuela.objects.all()
    context = {'escuelas':escuelas}
    return render(request, 'guardarCarrera.html', context)

def guardarEscuela(request):
    context = {}
    return render(request, 'guardarEscuela.html', context)
