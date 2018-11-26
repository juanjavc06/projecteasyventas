from django.shortcuts import render
from  .models import *
from .forms import *

# Create your views here.

def index(request):
	return render(request, "dashboard/dashboard.html")

def crear_producto(request):
	form = FormProductos(request.POST)
	context = {	'form':form	}

	return render(request,"templates/ecommerce-product-single.html", context)





def login(request):
	return render(request, "forms/login.html")

def startSellPoint(request):
	return render(request, "dashboard/sellpoint.html")
