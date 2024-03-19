from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    
    path('', views.home, name='home.html'),
    path('pagina1/', views.pagina1, name='pagina1.html'),
    path('pagina2/', views.pagina2, name='pagina2.html'),

    path('accounts/', include('django.contrib.auth.urls')) 

]
