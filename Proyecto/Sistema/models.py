from django.db import models


# Create your models here.
class Productos(models.Model):
    Codigo=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=25)
    Precio=models.FloatField(max_length=10)
    Descripcion=models.TextField(max_length=50)

    def __str__(self):
        return str(self.Codigo)

