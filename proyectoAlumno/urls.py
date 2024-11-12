"""proyectoAlumno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appAlumno import views as appAlumno
from appProfesor import views as appProfesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appAlumno.index),
    path('alumnos/', appAlumno.listarAlumnos),
    path('registrar/', appAlumno.registrarAlumnos),
    path('eliminarAlumno/<int:id>', appAlumno.eliminarAlumno),
    path('actualizarAlumno/<int:id>', appAlumno.actualizarAlumno),
    path('profesores/',appProfesor.listadoProfesor),
    path('agregarProfesor/',appProfesor.agregarProfesor),
    path('eliminarProfesor/<int:id>',appProfesor.eliminarProfesor),
    path('actualizarProfesor/<int:id>',appProfesor.actualizarProfesor),
    path('cursos/', appAlumno.listadoCursos),
    path('agregarCurso/', appAlumno.agregarCurso),
    path('actualizarCurso/<int:id>', appAlumno.actualizarCurso),
    path('eliminarCurso/<int:id>', appAlumno.eliminarCurso)
]
