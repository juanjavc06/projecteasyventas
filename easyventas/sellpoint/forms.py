from django import forms
from .models import *

class FormProductos(forms.ModelForm):

	class Meta:
		model 	= Productos
		fields 	= '__all__'
		widgets	= {'descripcion':forms.Textarea(attrs={'cols':50,'rows':5})}

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


