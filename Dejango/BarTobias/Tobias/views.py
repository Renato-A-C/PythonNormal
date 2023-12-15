from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template import loader
from reportlab.pdfgen import canvas
import io
from .models import Produto
from .forms import ProdutoForm


# Create your views here.


def lista_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"lista_produto.html", {'Produto': Produtos})

def criacaoProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('lista_produto')
            except:
                pass
    else:
        form = ProdutoForm()
    return render(request,'criar_Produto.html', {'form': form})

def alterar_produto(request,id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(initial={'nome': Produto.nome, 'descricao': Produto.DescProduto, 'preco': Produto.Preco, 'numNotaFiscal': Produto.NumNotaFiscal})
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('lista_produto')
            except Exception as e:
                pass
    return render(request,'alterar_produto.html', {'form' : form})

def deletar_produto(request,id):
    produto = Produto.objects.get(id=id)
    try:
        produto.delete()
    except:
        pass
    return redirect('lista_produto')
    