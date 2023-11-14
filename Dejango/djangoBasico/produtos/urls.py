from django.urls import path

from . import views

urlpatterns = [
    path('produtos', views.pagina_produtos),
    path('celulares/',views.celulares)
]
