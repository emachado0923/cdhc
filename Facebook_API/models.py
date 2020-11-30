from django.db import models


# Create your models here.

class User_Facebook(models.Model):
    email = models.CharField(max_length=50, unique=False)
    name = models.CharField(max_length=50, unique=False)
    birthday = models.CharField(max_length=50, unique=False)
    location = models.CharField(max_length=50, unique=False)
    gender = models.CharField(max_length=50, unique=False)
    picture = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return self.email


class Resultados(models.Model):
    Usuario = models.ForeignKey(User_Facebook, on_delete=models.CASCADE)
    correo = models.CharField(max_length=100, unique=False)
    Timestamp = models.CharField(max_length=50, unique=False)
    genero = models.CharField(max_length=15, unique=False)
    edad = models.CharField(max_length=15, unique=False)
    Tipo_baldosa = models.CharField(max_length=80, unique=False)
    Tipo_Salpicadero = models.CharField(max_length=200, unique=False)
    Tipo_Baño = models.CharField(max_length=100, unique=False)
    Tipo_Sala = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.correo


class Formularios(models.Model):
    nombreFormulario = models.CharField(max_length=50, unique=False)
    urlFormulario = models.CharField(max_length=200, unique=True)
    urlRespuestas = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=500, unique=True)
    estado = models.BooleanField(default=True)
