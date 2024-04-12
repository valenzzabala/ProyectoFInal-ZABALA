from django.db import models
from django.contrib.auth.models import User
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}   Camada: {self.camada}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    dni = models.CharField(max_length=10)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos')
    

    def __str__(self):
        return f"Nombre: {self.nombre}    Apellido:{self.apellido}    DNI: {self.dni}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    dni = models.CharField(max_length=10)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='profesores')
    

    def __str__(self):
        return f"Nombre: {self.nombre}    Apellido:{self.apellido}   DNI:{self.dni}     Curso a cargo:{self.curso}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)
    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"


