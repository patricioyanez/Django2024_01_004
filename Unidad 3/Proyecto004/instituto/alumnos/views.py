from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def listarAlumnos(request):
    # utilizar ORM de Django
    # select * from alumno
    alumnos = Alumno.objects.all()

    context = {'alumnos': alumnos}

    return render(request, 'index2.html', context)