from django.shortcuts import redirect, render
from appProfesor.models import Profesor
from appProfesor.forms import FormProfesor
# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoProfesor(request):
    profesores = Profesor.objects.all()
    data = {'profesores':profesores}
    return render(request,'profesores.html',data)

def agregarProfesor(request):
    form = FormProfesor()
    if request.method=='POST':
        form = FormProfesor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profesores')
    else:
        form = FormProfesor()
    data = {'form':form}
    return render(request,'agregarProfesor.html',data)

def eliminarProfesor(request,id):
    profesor = Profesor.objects.get(id = id)
    profesor.delete()
    return redirect('/profesores')

def actualizarProfesor(request,id):
    profesor= Profesor.objects.get(id = id)
    form = FormProfesor(instance=profesor)
    if request.method=='POST':
        form = FormProfesor(request.POST,instance=profesor)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'agregarProfesor.html',data)