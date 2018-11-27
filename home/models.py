from django.db import models

# Create your models here.

class Categoria (models.Model):
	nombre = models.CharField(max_length=100,unique=True)

	def __str__ (self):
		return self.nombre


class Bodega (models.Model):
	nombre = models.CharField(max_length=100,unique=True)
	foto = models.ImageField(upload_to='fotos',null = True, blank = True)

	def __str__ (self):
		return self.nombre


class Cuentadante (models.Model):
	nombre = models.CharField(max_length=100)
	identificacion = models.IntegerField(unique=True)

	def __str__ (self):
		return self.nombre
		

class Programa (models.Model):
	nombre = models.CharField(max_length=100,unique=True)

	def __str__ (self):
		return self.nombre


class Ficha (models.Model):
	numero_ficha = models.IntegerField(unique=True)
	fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
	fecha_finalizacion = models.DateField(auto_now=False, auto_now_add=False)
	estado= models.BooleanField(default=True)
	programa = models.ForeignKey(Programa, on_delete= models.CASCADE)

	def __str__ (self):
		return str(self.numero_ficha)

	#NO HAY CRUZ DE APRENDIZ

class Aprendiz (models.Model):
	nombre = models.CharField(max_length=100)
	identificacion = models.IntegerField(unique=True)
	tipo_documento = models.CharField(max_length=50)
	estado=models.BooleanField(default=True)
	ficha=models.ManyToManyField(Ficha,null=True,blank=True)

	def __str__ (self):
		return self.nombre
		
class Marca (models.Model):
	nombre = models.CharField(max_length=100,unique=True)

	def __str__ (self):
		return self.nombre

class Nombre_Material(models.Model):
	nombre = models.CharField(max_length=100,unique=True)

	def __str__(self):
		return self.nombre

class Material (models.Model):
	estado_choices=(
		('Disponible', 'Disponible'),
		('No Disponible', 'No Disponible'),
	)

	tipo_elemento = models.CharField(max_length=100)
	nombre = models.ForeignKey(Nombre_Material, on_delete=models.CASCADE)
	codigo_sena = models.CharField(max_length=100,unique=True,blank=True,null=True)
	numero_serie = models.CharField(max_length=100,unique=True,blank=True,null=True)
	cantidad = models.IntegerField(default=1,blank=True)
	estado = models.CharField(max_length=100,choices=estado_choices,default='Disponible')
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	cuentadante = models.ForeignKey(Cuentadante, on_delete=models.CASCADE)
	ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
	imagen=models.ImageField(upload_to='fotos',null = True, blank = True)

	def __str__ (self):
		return str(self.nombre)

class Bodega_Material(models.Model):
	material=models.ForeignKey(Material, on_delete=models.CASCADE)
	bodega=models.ForeignKey(Bodega, on_delete=models.CASCADE)
	fecha_ingresa=models.DateField(auto_now=False, auto_now_add=False)
	fecha_salida=models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

	def __str__ (self):
		return str(self.material)

class Prestamo (models.Model):
	fecha_prestamo = models.DateField(auto_now=False, auto_now_add=False)
	estado = models.CharField(max_length=50)	
	aprendiz = models.ForeignKey(Aprendiz, on_delete= models.CASCADE)
	fecha_entrega=models.DateField(auto_now=False, auto_now_add=False)

	def __str__ (self):
		return self.estado

class Detalle_Prestamo(models.Model):
	material=models.ForeignKey(Material, on_delete=models.CASCADE)
	prestamo=models.ForeignKey(Prestamo, on_delete=models.CASCADE)
	cantidad = models.IntegerField()

	estado_elemento_prestamo=models.CharField(max_length=50,null=True,blank=True)
	descripcion=models.TextField(max_length=1000,null=True,blank=True)
	tipo_daño=models.CharField(max_length=6,null=True,blank=True)
	estado_devolucion=models.CharField(max_length=50,null=True,blank=True)
	fecha_devolucion=models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

	def __str__ (self):
		return str(self.material)