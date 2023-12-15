from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_produto, name='lista_produto'),
    path('criar_produto/', views.criacaoProduto , name='criar_produto'),
    path('alterar_produto/', views.alterar_produto, name='alterar'),
    path('alterar_produto/<int:id>', views.alterar_produto, name='alterar_produto'),
    path('deletar_produto/', views.deletar_produto, name='deletar'), 
    path('deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
    path('consulta_produto/', views.consulta_produto, name='consulta_produto'),  
]
   