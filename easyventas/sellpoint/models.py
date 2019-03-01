from django.db import models
from django.conf import settings

# Create your models here.


class Categoria_Productos(models.Model):
	categoria 			= models.CharField(max_length=50)
	descripcion_categoria 		= models.CharField(max_length=255)

	def __str__(self):
		return str(self.categoria)

#--------------------------Seccion adan----------------------------------------------------
class Productos(models.Model):
	nombre 				= models.CharField(max_length=200)
	descripcion 		= models.CharField(max_length=500)
	unidad_medida 		= models.CharField(max_length=4)
	inventario_minimo	= models.FloatField()
	inventario_maximo	= models.FloatField()
	imagen 				= models.BinaryField(blank=True)
	precio 				= models.FloatField()
	categoria 	        = models.ForeignKey(Categoria_Productos, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nombre)




class Proveedores_Clientes(models.Model):
	nombre_comercial = models.CharField(max_length=255)
	rfc				 = models.CharField(max_length=18)
	direccion 		 = models.CharField(max_length=255)
	tipo 			 = models.BooleanField()


	def __str__(self):
		return str(self.rfc)

class Productos_Proveedores(models.Model):
	producto 		 = models.ForeignKey(Productos, on_delete=models.CASCADE)
	proveedor 		 = models.ForeignKey(Proveedores_Clientes, on_delete=models.CASCADE)
	cantidad  		 = models.IntegerField()
	costo_total 	 = models.FloatField()

	def __str__(self):
		return str(self.id)


class Compras(models.Model):
	fecha 			= models.DateField(auto_now_add=True)
	sub_total		= models.FloatField()
	impuestos 		= models.FloatField()
	total 			= models.FloatField()
	fecha_entrega	= models.DateField()
	proveedor 		= models.ForeignKey(Proveedores_Clientes,on_delete=models.CASCADE, blank= True)

	def __str__(self):
		return str(self.id)

class  Compras_Detalle(models.Model):
	compra 			= models.ForeignKey(Compras, on_delete=models.CASCADE)
	producto  	= models.ForeignKey(Productos, on_delete=models.CASCADE)
	cantidad 		= models.FloatField()
	total_producto  = models.FloatField()

	def __str__(self):
		return str(self.id)


class Ventas(models.Model):
	fecha 	 		= models.DateTimeField(auto_now_add=True)
	sub_total		= models.FloatField()
	impuestos 		= models.FloatField()
	total 			= models.FloatField()
	cliente 		= models.ForeignKey(Proveedores_Clientes, on_delete=models.CASCADE, blank = True,default=None)
	def __str__(self):
		return str(self.id)


class Ventas_Detalle(models.Model):
	venta 			= models.ForeignKey(Ventas, on_delete=models.CASCADE)
	producto 		= models.ForeignKey(Productos, on_delete=models.CASCADE)
	cantidad 		= models.FloatField()
	total_producto  = models.FloatField()

	def __str__(self):
		return str(self.id)


#--------------------------Seccion Jenny no tocar :v ---------------------------------------

#class Perfiles(models.Model):
#	perfil 			= models.CharField(max_length=100)
#
#	def __str__(self):
#		return str(self.perfil)


#class Usuarios(models.Model):
#	usuarios 		= models.CharField(max_length=255)
#	nombre 			= models.CharField(max_length=255)
#	password		= models.CharField(max_length=100)
#	perfil 			= models.ForeignKey(Perfiles,on_delete=models.CASCADE)

#	def __str__(self):
#		return str(self.usuarios)
		
class Almacen(models.Model):
	almacen 		= models.CharField(max_length=255)
	
	def __str__(self):
		return str(self.almacen)

class Zona(models.Model):
	zona 			= models.CharField(max_length=255)
	almacen 		= models.ForeignKey(Almacen,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.zona)

class Inventario(models.Model):
	existencias 	= models.IntegerField()
	producto  		= models.ForeignKey(Productos,on_delete=models.CASCADE)
	zona 			= models.ForeignKey(Zona,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)



class Movimientos(models.Model):
	tipo 			= models.CharField(max_length=255)
	producto 		= models.CharField(max_length=200)
	fecha 			= models.DateTimeField(auto_now_add=True)
	cantidad 		= models.IntegerField()
	zona 			= models.ForeignKey(Zona,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)



class Corte(models.Model):
	fecha 			= models.DateTimeField(auto_now_add=True)
	total_vendido 	= models.IntegerField()
	total_comprado	= models.IntegerField()

	def __str__(self):
		return str(self.id)


class Detalle_Corte(models.Model):
	producto 		= models.CharField(max_length=200)
	cantidad 		= models.IntegerField()
	total 			= models.FloatField()
	iva 			= models.FloatField()
	corte 			= models.ForeignKey(Corte, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)
