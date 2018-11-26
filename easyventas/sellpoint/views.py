from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "dashboard/dashboard.html")

def login(request):
	return render(request, "forms/login.html")

def startSellPoint(request):
	return render(request, "dashboard/sellpoint.html")
