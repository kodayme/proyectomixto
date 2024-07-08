from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField()
    tlf = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nombre

class articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"nombre de la merca: {self.nombre} de la sección {self.seccion} que cuesta {self.precio}$"



class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrega = models.BooleanField()

# ====================================TABLA SERVICIOS============================================================================================

class Servicios(models.Model):

    titulo = models.CharField(max_length=30)
    contenido = models.TextField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo
# ==============================================================================================================================================

# ====================================TABLA CATEGORIAS============================================================================================

class Categoria(models.Model):
    nombre_categorico = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre_categorico

# ================================================================================================================================================
# ====================================TABLA CONTENIDOS============================================================================================


class Contenido(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField()
    link = models.CharField(max_length=1000)
    categorias = models.ManyToManyField(Categoria)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"

    def __str__(self):
        return self.nombre
# =================================================================================================================================================

# =======================================================TABLA TIENDA============================================================================


class categoria_tienda(models.Model):
    nombre = models.CharField(max_length=100,)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria_tienda"
        verbose_name_plural = "categorias_tiendas"

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categoria_tienda, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes_tienda")
    precio = models.IntegerField()
    descripcion = models.TextField(null=True,blank=True)
    disponibilidad = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

# =================================================================================================================================================

# =============================================TABLE DE PEDIDOS==================================================================================











# =================================================================================================================================================