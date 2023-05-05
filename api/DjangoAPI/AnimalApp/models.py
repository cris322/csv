from django.db import models

# Create your models here.
class perritos(models.Model):
    IdPerro = models.AutoField(primary_key=True)
    nombrePerro = models.CharField(max_length=500)
    razaPerro = models.CharField(max_length=500)
    edadPerro = models.CharField(max_length=500)

class accesorios(models.Model):
    IdAccesorio = models.AutoField(primary_key=True)
    nombreAccesorio = models.CharField(max_length=500)    
    cantidadAccesorio = models.CharField(max_length=500)
    precioAccesorio = models.CharField(max_length=500) 