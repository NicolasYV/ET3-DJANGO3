from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)

class Usuario(models.Model):
    # rut - Nombre - AppPaterno - appMaterno - fecha Nacimiento
    # tipo - correo - telefono - activo
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    tipoUsuario = models.ForeignKey(
        'tipoUsuario', on_delete=models.CASCADE, db_column='idTipo')
    correo = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.appPaterno)+" "+str(self.appMaterno)
    
    
class Cliente(models.Model):
    rutCliente = models.CharField(max_length=10, primary_key=True)
    nombreCliente = models.CharField(max_length=50, blank=False, null=False)
    emailCliente = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    telefonoCliente = models.CharField(max_length=10, blank=False, null=False)

    
    def __str__(self):
        return str(self.nombreCliente)
    
    
    
class Producto(models.Model):
    idProducto =  models.CharField(max_length=12, primary_key=True)
    nombreProducto = models.CharField(max_length=50, blank=False, null=False)
    cantidad = models.CharField(max_length=100)
    precio = models.CharField(max_length=100000)
    estadoProducto = models.IntegerField()

    def __str__(self):
        return str(self.nombreProducto)
    
    
#class Promocion(models.Model):
#    productosPromocion = 
    
    
#class Descuento(models.Model):
#    descuento = 





# Create your models here.
