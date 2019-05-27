from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre

class Login(models.Model):
    Usuario = models.CharField(max_length= 10, unique=True)
    Password = models.CharField(max_length=10)

class Carrito(models.Model):
    modelo = models.CharField(max_length = 30, unique = True)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    Total = models.IntegerField(default=0)

class Celular(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 30, unique = True)
    precio = models.IntegerField()
    memoria = models.CharField(max_length = 20, default='')
    camarafrontal = models.CharField(max_length = 20, default='')
    camaratrasera = models.CharField(max_length = 20, default='') 
    cpu = models.CharField(max_length = 20)
    os = models.CharField(max_length = 20)
    srcimg = models.CharField(max_length = 200, default = "")
    idpaypal = models.CharField(max_length=20, default="")
    idpaypalcarrito = models.CharField(max_length=20, default="")
    


    
    def __str__(self):
        return self.modelo
    
    class Meta:
        verbose_name="Celular"
        verbose_name_plural = "Celulares"
