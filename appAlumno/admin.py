from django.contrib import admin
from appAlumno.models import Alumno, Curso, Matricula
from appProfesor.models import Profesor

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'direccion', 'telefono', 'edad']
    filter_horizontal = ('cursos',)  # Esto ya lo tienes, para mostrar los cursos asociados al alumno
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'direccion', 'telefono']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'horas', 'descripcion', 'fecha_inicio', 'fecha_fin', 'seccion', 'profesor']

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['alumno', 'curso', 'fecha_matricula']
    list_filter = ['fecha_matricula']  # Para filtrar por fecha de matrícula

# Registrar los modelos
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)  # Registrar el modelo Matricula
