from django.urls import path

from . import views

urlpatterns = [
    path('', views.car_price, name='car_price'),
    path('result/', views.result, name='result'),
]