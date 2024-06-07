from django.urls import path
from . import views

#http://127.0.0.1:8000/alumnos/index
urlpatterns = [
    path('', views.menu , name='menu'),
    path('index', views.index , name='index'),
    path('listarAlumno', views.listarAlumno , name='listarAlumno'),
    path('listarEscuela', views.listarEscuela , name='listarEscuela'),
    path('listarCarrera', views.listarCarrera , name='listarCarrera'),
    path('guardarCarrera', views.guardarCarrera , name='guardarCarrera'),
    path('guardarEscuela', views.guardarEscuela , name='guardarEscuela'),
    path('buscarEscuela/<str:pk>', views.buscarEscuela , name='buscarEscuela'),
    path('eliminarEscuela/<str:pk>', views.eliminarEscuela , name='eliminarEscuela'),
    path('eliminarCarrera/<str:pk>', views.eliminarCarrera , name='eliminarCarrera'),
]