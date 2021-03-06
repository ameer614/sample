"""ameerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from vali import views
from django.conf import settings
from .models import Productmodel

urlpatterns = [
    path('category/<int:category>/',views.web),
    path('home/',views.home),
    # path('show/<int:id>/',views.product),
    path('web/',views.web),
    path('add/',views.create_prodect),
    path('edit/<int:id>/',views.update_prodect),
    path('delete/<int:id>/',views.delete_product),
    path('test/',views.test),
    path('create_user/',views.create_user),
    path('login/',views.User_login),
    path('logout/',views.user_logout)

]

