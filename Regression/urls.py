from django.urls import path

from . import views

urlpatterns = [
    path('', views.regression, name='regression'),
    path('carprice/', views.car_price, name='car_price'),
    path('carprice/result/', views.result, name='result'),
]
