from django.db import models

# Create your models here.
class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre= models.CharField(max_length=50, null= False, blank= False)
    apellido= models.CharField(max_length=50, null= False, blank= False)
    fecha_nacimiento= models.DateTimeField(null= False, blank= False)
    
    def __str__(self) -> str:
        return f"({self.rut}) - {self.nombre} {self.apellido}"

class Direccion(models.Model):
    calle= models.CharField(max_length=50, null= False, blank= False)
    numero= models.CharField(max_length=10, null= False, blank= False)
    dpto= models.CharField(max_length=10, null= True, blank= True)
    comuna= models.CharField(max_length=50, null= False, blank= False)
    ciudad= models.CharField(max_length=50, null= False, blank= False)
    region= models.CharField(max_length=50, null= False, blank= False)
    conductor = models.OneToOneField(Conductor,null= False, blank= False, on_delete= models.CASCADE )#FK uno a uno

    def __str__(self) -> str:
        return f"{self.calle} #{self.numero}"
    
class Vehiculo(models.Model):
    patente= models.CharField(max_length=6, null= False, blank= False, unique= True)
    marca= models.CharField(max_length=50, null= False, blank= False)
    modelo= models.CharField(max_length=50, null= False, blank= False)
    year = models.IntegerField(null= False, blank= False)
    conductor = models.ForeignKey(Conductor,null= False, blank= False, on_delete= models.CASCADE )#FK uno a muchos

    def __str__(self) -> str:
        return f"({self.id}) - {self.patente}"