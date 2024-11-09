from django import forms
from appProfesor.models import Profesor
from django.core.exceptions import ValidationError

class FormProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
