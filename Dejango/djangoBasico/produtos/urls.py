from django.urls import path
from . import views

# produtos/
urlpatterns = [
    path('', views.index),
    path('celulares/', views.celulares),
]