from django.shortcuts import render

from alumnos.forms import UsuarioForm
from .models import Alumno,Escuela,Carrera, Usuario

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    context = {}
    return render(request, 'plantillaBase.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)
@login_required
def listarAlumno(request):
    # utilizar ORM de Django
    # select * from alumno
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'listarAlumno.html', context)

@login_required
def listarEscuela(request):
    # utilizar ORM de Django
    # select * from alumno
    listado = Escuela.objects.all()
    context = {'listado': listado}
    return render(request, 'listarEscuela.html', context)
@login_required
def listarCarrera(request):
    # utilizar ORM de Django
    # select * from alumno
    listado = Carrera.objects.all()
    context = {'listado': listado}
    return render(request, 'listarCarrera.html', context)
@login_required
def guardarEscuela(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST # v o F

        if 'btnGuardar' in request.POST:
            # validar...
            if len(nombre.strip()) < 1:
                context['error'] = 'No especificó el nombre'
            else:
                if id == "0":
                    Escuela.objects.create(nombre=nombre, activo=activo)
                else:
                    item = Escuela()
                    item.id = id
                    item.nombre = nombre
                    item.activo = activo
                    item.save()

                context['exito'] = "Los datos fueron guardados"

    return render(request, 'guardarEscuela.html', context)
@login_required
def guardarCarrera(request):
    context = {}
    context['escuelas'] = Escuela.objects.all()

    if request.method == 'POST':
        idEscuela =  request.POST['cmbEscuela']
        nombre = request.POST['txtNombre']
        version = request.POST['txtVersion']
        activo = 'chkActivo' in request.POST # v o F


        if 'btnGuardar' in request.POST:
            # TAREA: validar y capturar excepciones
            escuela = Escuela.objects.get(pk= idEscuela) # buscar obj según id seleccionado
            Carrera.objects.create(escuela= escuela,
                                    nombre=nombre, 
                                    version=version, 
                                    activo=activo)

            context['exito'] = "Los datos fueron guardados"
    return render(request, 'guardarCarrera.html', context)
@login_required
def guardarUsuario(request):
    context = {'form': UsuarioForm()}

    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            form = UsuarioForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                context['exito'] = 'Datos Guardados'
            else:
                context['error'] = 'Error al guardar los datos'
                
    context['listado'] = Usuario.objects.all()
    return render(request, 'guardarUsuarioForm.html', context)
@login_required
def eliminarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk=pk)
        item.delete()
        context['exito'] = 'Escuela eliminada con éxito'
    except:
        context['error'] = 'Error al tratar de eliminar la información'
        
    listado = Escuela.objects.all()
    context['listado'] = listado
    return render(request, 'listarEscuela.html', context)
@login_required
def eliminarCarrera(request, pk):
    context = {}
    try:
        item = Carrera.objects.get(pk=pk)
        item.delete()
        context['exito'] = 'Carrera eliminada con éxito'
    except:
        context['error'] = 'Error al tratar de eliminar la información'
        
    listado = Carrera.objects.all()
    context['listado'] = listado
    return render(request, 'listarCarrera.html', context)
@login_required
def eliminarUsuario(request, pk):
    context = {}
    try:
        item = Usuario.objects.get(pk=pk)
        item.delete()
        context['exito'] = 'El item fue eliminado con éxito'
    except:
        context['error'] = 'Error al tratar de eliminar la información'
        
    context['listado'] = Usuario.objects.all()
    context['form'] = UsuarioForm()
    return render(request, 'guardarUsuarioForm.html', context)

@login_required
def buscarEscuela(request, pk):
    context = {}
    try:
        context['item'] = Escuela.objects.get(pk=pk)
    except:
        context['error'] = 'Error al buscar información'

    return render(request, 'guardarEscuela.html', context)
        