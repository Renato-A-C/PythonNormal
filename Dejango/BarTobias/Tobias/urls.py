from django.urls import path, include
from django.conf import settings
from . import views
from .views import relatorio_pdf

urlpatterns = [
    # Janelas principais
    path("", views.home, name="home"),
    path("principal", views.principal, name="principal"),
    
    # Crud produto
    path('cruproduto/lista_produto/', views.lista_produto, name='lista_produto'),
    path('cruproduto/criar_produto/', views.criacaoProduto , name='criar_produto'),
    path('cruproduto/alterar_produto/', views.alterar_produto, name='alterar_prod'),
    path('cruproduto/alterar_produto/<int:id>', views.alterar_produto, name='alterar_produto'),
    path('cruproduto/deletar_produto/', views.deletar_produto, name='deletar_produto'), 
    path('cruproduto/deletar_produto/<int:id>', views.deletar_produto, name='deletar'),
    path('cruproduto/consulta_produto/', views.consulta_produto, name='consulta_produto'), 
    
    # Crud de funcionários
    path("crufunc/lista_funcionario", views.lista_funcionario, name="lista_funcionario"),
    path("registration/cad_funcionario", views.cad_funcionario, name="cad_funcionario"),
    path("crufunc/alterar_funcionario", views.alterar_funcionario, name="alterar_func"),
    path("crufunc/alterar_funcionario/<int:id>", views.alterar_funcionario, name="alterar_funcionario"),
    path("crufunc/deletar_funcionario", views.deletar_funcionario, name="deletar_func"),
    path("crufunc/deletar_funcionario/<int:id>", views.deletar_funcionario, name="deletar_funcionario"),
    
    # Crud para vendas
    path("cruvenda/venda", views.venda, name="venda"),
    path("cruvenda/lista_venda", views.lista_venda, name="lista_venda"),
    path("cruvenda/criar_venda2", views.criar_venda2, name="criar_venda2"),
    path("cruvenda/criar_venda/<int:id>", views.criar_venda, name="criar_venda"),
    path("cruvenda/addp/<int:id>", views.addp, name="addp"),
    # Crud para cliente
    
    path("crucliente/lista_cliente", views.lista_cliente, name="lista_cliente"),
    path("crucliente/alterar_cliente", views.alterar_cliente, name="alterar_cli"),
    path("crucliente/alterar_cliente/<int:id>", views.alterar_cliente, name="alterar_cliente"),
    path("crucliente/deletar_cliente", views.deletar_cliente, name="deletar_cli"),
    path("crucliente/deletar_cliente/<int:id>", views.deletar_cliente, name="deletar_cliente"),
    # Views gerais
    path('relatorios/relatorio/', relatorio_pdf.as_view(), name='relatorio_pdf'),
    
    #janela de administração geral
    path('accounts/', include('django.contrib.auth.urls')) 

]
