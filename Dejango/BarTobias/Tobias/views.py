from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
import io
from .models import Produto
from .forms import ProdutoForm


# Create your views here.
def home(request):

    return render(request,"home.html")

@login_required
def principal(request):
    Produtos = Produto.objects.all()
    return render(request,"principal.html", {'Produto': Produtos})

@login_required
def venda(request):
    Produtos = Produto.objects.all()
    return render(request,"venda.html", {'Produto': Produtos})
@login_required
def lista_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"cruproduto/lista_produto.html", {'Produto': Produtos})

@login_required
def criacaoProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                
                return redirect('lista_produto')
            except:
                pass
    else:
        form = ProdutoForm()
    return render(request,"cruproduto/criar_Produto.html", {'form': form})


@login_required
def alterar_produto(request,id):

    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        produto.nomeProduto = request.POST.get('nomeProduto')
        
        produto.precoProduto = request.POST.get('precoProduto')
      
        produto.quantidadeProduto = request.POST.get('quantidadeProduto')
        produto.save()
        messages.success(request, "produto alterado")
        return redirect('lista_produto')
    context = {
        'Produto': produto,
               
    }
    return render(request,'cruproduto/alterar_produto.html',context)


@login_required
def deletar_produto(request,id):
    produto = Produto.objects.get(id=id)
    try:
        produto.delete()
    except:
        pass
    return redirect('lista_produto')

@login_required
def consulta_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"cruproduto/consulta_produto.html", {'Produto': Produtos})