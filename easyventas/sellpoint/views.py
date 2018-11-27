from django.shortcuts import render
from crispy_forms.helper import FormHelper

from  .models import *
from .forms import *

# Create your views here.

def index(request):
	return render(request, "dashboard/dashboard.html")

def login(request):
	return render(request, "forms/login.html")

def startSellPoint(request):
	return render(request, "dashboard/sellpoint.html")

def crear_producto(request):
	form = FormProductos(request.POST)
	context = {	'form':form	}
	return render(request,"dashboard/productos_crear.html", context)

def form_productos_view(request):
	form = FormProductos(request.POST)
	context = {	'form':form	}
	return render(request,"dashboard/form_productos.html", context)
