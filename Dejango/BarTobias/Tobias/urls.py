from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listagem/", views.listagem, name="listagem"),
    path("cad/", views.cad, name="cad"),
    
]
