from django.urls import path
from . import views

# clientes/
urlpatterns = [
    path('', views.index),
    path('emails/', views.emails),
]