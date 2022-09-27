from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('regression/', views.regression, name='regression'),
    path('classification/', views.classification, name='classification'),
]
