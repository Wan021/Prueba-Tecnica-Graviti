from django.db import models

# Create your models here.

class Persona(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido_paterno=models.CharField(max_length=50)
    apellido_materno=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=30)
    edad=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} {1} {2} ({3})"
        return texto.format(self.apellido_paterno, self.apellido_materno, self.nombre, self.nacionalidad)

