from django import forms
from .models import *

class FormProductos(forms.ModelForm):

	class Meta:
		model 	= Productos
		fields 	= '__all__'
		widgets	= {'descripcion':forms.Textarea(attrs={'cols':30,'rows':3})}

class FormCategoria_Productos(forms.ModelForm):

	class Meta:
		model 	= Productos
		fields 	= '__all__'
		widgets	= {'descripcion':forms.Textarea(attrs={'cols':50,'rows':5})}



class FormProveedores_Clientes(forms.ModelForm):
	class Meta:
		model 	= Proveedores_Clientes
		fields	= '__all__'


class FormProductos_Proveedores(forms.ModelForm):
	class Meta:
		model 	= Productos_Proveedores
		fields	= '__all__'

class FormCompras(forms.ModelForm):
	class Meta:
		model 	= Compras
		fields	= '__all__'


class FormCompras_Detalle(forms.ModelForm):
	class Meta:
		model 	= Compras_Detalle
		fields	= '__all__'

class FormVentas(forms.ModelForm):
	class Meta:
		model 	= Ventas
		fields	= '__all__'



class FormVentas_Detalle (forms.ModelForm):
	class Meta:
		model 	= Ventas_Detalle
		fields	= '__all__'

#-------------------------------------------Seccion Jenny--------------------------------------------------
class FormPerfiles(forms.ModelForm):

	class Meta:
		model  = Perfiles
		fields = '__all__'

class FormUsuarios(forms.ModelForm):

	class Meta:
		model  = Usuarios
		fields = '__all__'

class FormZona(forms.ModelForm):

	class Meta:
		model  = Zona
		fields = '__all__'


class FormInventario(forms.ModelForm):

	class Meta:
		model  = Inventario
		fields = '__all__'

class FormAlmacen(forms.ModelForm):

	class Meta:
		model   = Almacen
		fields	= '__all__'


class FormMovimientos(forms.ModelForm):

	class Meta:
		model   = Movimientos
		fields	= '__all__'

class FormCorte(forms.ModelForm):

	class Meta:
		model      = Corte
		fields     = '__all__'
