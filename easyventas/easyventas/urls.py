"""easyventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sellpoint import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login ,name="index"),
    path('dashboard/', views.index ,name="index"),
    path('', admin.site.urls),
    path('articulos/', admin.site.urls),
    path('crear_productos/', views.crear_producto, name="crear_producto_view"),

]
