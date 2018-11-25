from django.db import models
from django.conf import settings

# Create your models here.
class Productos(models.Model):
	nombre 				= models.CharField(max_length=200)
	descripcion 		= models.CharField(max_length=500)
	unidad_medida 		= models.CharField(max_length=4)
	inventario_minimo	= models.FloatField()
	inventario_maximo	= models.FloatField()
	imagen 				= models.BinaryField(blank=True)
	precio 				= models.FloatField()

	def __str__(self):
		return str(self.nombre)


class Categoria_Productos(models.Model):
	nombre 			= models.CharField(max_length=50)
	descripcion 	= models.CharField(max_length=255)

	def __str__(self):
		return str(self.nombre)

class Compras(models.Model):
	fecha 			= models.DateField(auto_now_add=True)
	sub_total		= models.FloatField() 
	impuestos 		= models.FloatField()
	total 			= models.FloatField()
	fecha_entrega	= models.DateField()
	""" proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE = True)  """

	def __str__(slef):
		return str(self.id)

class  Compras_Detalle(models.Model):
	compra 			= models.ForeignKey(Compras, on_delete=models.CASCADE)
	producto 		= models.ForeignKey(Productos, on_delete=models.CASCADE)
	cantidad 		= models.FloatField()
	total_producto  = models.FloatField()

	def __str__(self):
		return str(self.id)

class Ventas(models.Model):
	fecha 	 		= models.DateTimeField(auto_now_add=True)
	sub_total		= models.FloatField() 
	impuestos 		= models.FloatField()
	total 			= models.FloatField()
	"""cliente 		= models.ForeignKey(Proveedores_Clientes, on_delete=models.CASCADE, blank = True)"""
	def __str__(self):
		return str(self.id)


class Ventas_Detalle(models.Model):
	venta 			= models.ForeignKey(Ventas, on_delete=models.CASCADE)
	producto 		= models.ForeignKey(Productos, on_delete=models.CASCADE)
	cantidad 		= models.FloatField()
	total_producto  = models.FloatField()

	def __str__(self):
		return str(self.id)

