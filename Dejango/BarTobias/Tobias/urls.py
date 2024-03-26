from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("principal", views.principal, name="principal"),
    path('cruproduto/lista_produto/', views.lista_produto, name='lista_produto'),
    path('cruproduto/criar_produto/', views.criacaoProduto , name='criar_produto'),
    path('cruproduto/alterar_produto/', views.alterar_produto, name='alterar'),
    path('cruproduto/alterar_produto/<int:id>', views.alterar_produto, name='alterar_produto'),
    path('cruproduto/deletar_produto/', views.deletar_produto, name='deletar_produto'), 
    path('cruproduto/deletar_produto/<int:id>', views.deletar_produto, name='deletar'),
    path('cruproduto/consulta_produto/', views.consulta_produto, name='consulta_produto'), 
    path("venda/", views.venda, name="venda"),
    
    
    path('accounts/', include('django.contrib.auth.urls')) 

]
