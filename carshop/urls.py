"""carshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter

from premiumcars.views import index, add_car, all_cars, del_car, CarsView, edit

router = SimpleRouter()
router.register('api/cars', CarsView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('addcar/', add_car),
    path('allcars/', all_cars),
    path('delcar/', del_car),
    path(r'edit/<pk>', edit, name='edit')
]
urlpatterns += router.urls
