from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()



class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'correo', 'dni', 'curso']


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'correo', 'dni', 'curso']


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields= ['email','password1','password2']
        help_text = {k:"" for k in fields}

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario:'
        self.fields['username'].help_text = '150 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente.'
        self.fields['password1'].label = 'Contraseña:'
        self.fields['password1'].help_text = 'Tu contraseña debe tener al menos 8 caracteres y no ser demasiado común.'
        self.fields['password2'].label = 'Confirmar contraseña:'
        self.fields['password2'].help_text = 'Ingresa la misma contraseña que antes para verificar.'

        