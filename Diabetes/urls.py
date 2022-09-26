from django.urls import path

from . import views

urlpatterns = [
    path('', views.diabetes, name='diabetes'),
    path('result/', views.result, name='result'),
]