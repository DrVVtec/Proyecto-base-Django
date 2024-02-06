from django.db import models
#from datetime import date
from django.utils import timezone

# Create your models here.

class Proyecto(models.Model):
  name = models.CharField(max_length=200)
  tipo = models.CharField(max_length=20,default="Interno")
  responsable = models.CharField(max_length=100, default="David V.")
  
class Tarea(models.Model):
  titulo = models.CharField(max_length=200)
  descripcion = models.TextField()
  proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
  prioridad = models.IntegerField(default=0)
  fecha_asignacion = models.DateField(default=timezone.now())
  fecha_limite = models.DateField(default=timezone.now())
  fecha_entrega = models.DateField(default=timezone.now())
  
