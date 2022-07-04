from statistics import mode
from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=8)
    estado = models.BooleanField()

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos
