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
from django.urls import path, include
from sellpoint import views
from sellpoint import urls as sellpoint_urls

urlpatterns = [
    path('login/', views.login ,name="index"),
    path('dashboard/', views.index ,name="index"),
    path('articulos/', admin.site.urls),
    path('sellpoint/', views.startSellPoint),
    path('productos/nuevo/', views.form_productos_view, name="productos_nuevo"),
    path('admin/',admin.site.urls),
    path('',include(sellpoint_urls)),
]
