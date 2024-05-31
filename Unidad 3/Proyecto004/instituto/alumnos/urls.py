from django.urls import path
from . import views

#http://127.0.0.1:8000/alumnos/index
urlpatterns = [
    path('', views.menu , name='menu'),
    path('index', views.index , name='index'),
    path('listarAlumnos', views.listarAlumnos , name='listarAlumnos'),
    path('listarEscuela', views.listarEscuela , name='listarEscuela'),
    path('listarCarrera', views.listarCarrera , name='listarCarrera'),
    path('GuardarCarrera', views.GuardarCarrera , name='GuardarCarrera'),
]