from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.template import loader
from reportlab.pdfgen import canvas
import io
from .models import Produto
from .forms import ProdutoForm


# Create your views here.


def lista_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"core/lista_produto.html", {'Produto': Produtos})
@login_required
def tela_login(requests):
    Produtos = Produto.objects.all()
    return render(requests,"registration/tela_login.html")
@login_required
def tela_logout(requests):
    Produtos = Produto.objects.all()
    return render(requests,"registration/tela_logout.html")

def criacaoProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('core/lista_produto')
            except:
                pass
    else:
        form = ProdutoForm()
    return render(request,'core/criar_Produto.html', {'form': form})


def alterar_produto(request,id):
    produto = Produto.objects.get(id=id)
    
    form = ProdutoForm(initial={'nome': Produto.nome_do_produto, 'descricao': Produto.Descricao_do_Produto, 'preco': Produto.Preco_do_produto, 'numNotaFiscal': Produto.Numero_de_Nota_Fiscal, 'Quantidade_de_produtos': Produto.Quantidade_de_Produtos})
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        visao = ProdutoForm(request, instance=produto)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('core/lista_produto')
            except Exception as e:
                pass
    return render(request,'core/alterar_produto.html', {'form' : form, 'Produto': produto})

def deletar_produto(request,id):
    produto = Produto.objects.get(id=id)
    try:
        produto.delete()
    except:
        pass
    return redirect('core/lista_produto')


def consulta_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"core/consulta_produto.html", {'Produto': Produtos})