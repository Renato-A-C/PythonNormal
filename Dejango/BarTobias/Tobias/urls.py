from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.lista_produto, name='core/lista_produto'),
    path('criar_produto/', views.criacaoProduto , name='core/criar_produto'),
    path('alterar_produto/', views.alterar_produto, name='alterar'),
    path('alterar_produto/<int:id>', views.alterar_produto, name='core/alterar_produto'),
    path('deletar_produto/', views.deletar_produto, name='deletar'), 
    path('deletar_produto/<int:id>', views.deletar_produto, name='core/deletar_produto'),
    path('consulta_produto/', views.consulta_produto, name='core/consulta_produto'), 
    path('login/', views.tela_login, name='registration/tela_login'),
    path('logout/', views.tela_logout, name='registration/tela_logout'),
    path('accounts/', include('django.contrib.auth.urls')) 

]
