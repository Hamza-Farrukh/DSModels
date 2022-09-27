from django.urls import path

from . import views

urlpatterns = [
    path('', views.classification, name='classification'),
    path('diabetes/', views.diabetes, name='car_price'),
    path('diabetes/result/', views.result, name='result'),
]
