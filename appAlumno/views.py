from django.shortcuts import render, redirect
from appAlumno.models import Alumno, Curso
from appAlumno.forms import FormularioAlumno, FormularioCurso

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarAlumnos(request):
    alumnos = Alumno.objects.all
    data = {'alumnos':alumnos}
    return render(request, 'listadoAlumnos.html', data)

def registrarAlumnos(request):
    form = FormularioAlumno()
    if request.method == 'POST':
        form = FormularioAlumno(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = FormularioAlumno()
    data = {'form':form}
    return render(request, 'registrarAlumnos.html', data)

def eliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('/alumnos')

def actualizarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    form = FormularioAlumno(instance=alumno)
    if request.method == 'POST':
        form = FormularioAlumno(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = FormularioAlumno(instance=alumno)
    data = {'form':form}
    return render(request, 'registrarAlumnos.html', data)

# Cursos
def listadoCursos(request):
    cursos = Curso.objects.all
    data = {'cursos':cursos}
    return render(request, 'listadoCursos.html', data)

def agregarCurso(request):
    form = FormularioCurso()
    if request.method == 'POST':
        form = FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        FormularioCurso()
    data = {'form':form}
    return render(request, 'agregarCurso.html', data)

def eliminarCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/cursos')

def actualizarCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = FormularioCurso(instance=curso)
    if request.method == 'POST':
        form = FormularioCurso(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = FormularioCurso(instance=curso)
    data = {'form':form}
    return render(request, 'agregarCurso.html', data)