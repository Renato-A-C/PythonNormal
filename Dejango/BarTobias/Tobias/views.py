from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Produto, Cliente, Funcionario, Venda, LinkUser, CustomUser
from .forms import ProdutoForm, ClienteForm, FuncionarioForm, VendaForm, CustomUserForm, LinkUserForm


# Create your views here.
def home(request):

    return render(request,"home.html")

@login_required
def principal(request):
    Produtos = Produto.objects.all()
    return render(request,"principal.html", {'Produto': Produtos})

# views para produtos
@login_required
def lista_produto(request):
    Produtos = Produto.objects.all()
    context ={
        'Produto':Produtos
        
    }
    return render(request,"cruproduto/lista_produto.html", context)
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

    produto.excluido = True
    produto.save()
    return redirect('lista_produto')

@login_required
def consulta_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"cruproduto/consulta_produto.html", {'Produto': Produtos})


"""
# views para funcionario
"""

@login_required
def lista_funcionario(request):
    funcionario = CustomUser.objects.all()
    return render(request,"crufunc/lista_funcionario.html", {'Funcionario': funcionario})

@login_required
def cad_funcionario(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        func1 = FuncionarioForm(request.POST)
        func2 = LinkUserForm(request.POST)
        if form.is_valid() and func1.is_valid() and func2.is_valid():
            try:
                
                user = form.save()
                func = func1.save(commit=False)
                func.autor = user
                func.save()
                
                funcData = func2.save(commit=False)
                funcData.funcionario = func
                funcData.save()
                
                return redirect('cad_funcionario')
            except:
                pass
    else:
        form = CustomUserForm()
        func1 = FuncionarioForm()
        func2 = LinkUserForm()
    context = {
        'form':form,
        'func1':func1,
        'func2':func2
    }
        
    return render(request,"registration/cad_funcionario.html", context)

@login_required
def deletar_funcionario(request,id):
    funcionario = Funcionario.objects.get(id=id)
    try:
        funcionario.delete()
    except:
        pass
    return redirect('lista_funcionario')

@login_required
def alterar_funcionario(request, id):
    funcionario = CustomUser.objects.get(id=id)
    modeloUser = CustomUser.objects.get(id=id)
    linhaFuncionario = Funcionario.objects.get(autor=funcionario.id)
    
    linhaMulti= LinkUser.objects.get(funcionario=linhaFuncionario.id)

    print(f" aaaaa {funcionario.nome}")
    if request.method == "POST":
        instUser = CustomUserForm(request.POST) 
        instFuncionario = FuncionarioForm(request.POST)

        instMulti = LinkUserForm(request.POST)
        
        if instUser.is_valid() and instFuncionario.is_valid() and instMulti.is_valid():
            instUser.nome.save()
            instFuncionario.save()
            instMulti.save()
            return redirect('lista_funcionario')
    else:
        instUser = CustomUserForm() 
        instFuncionario = FuncionarioForm()
        instMulti = LinkUserForm()     
                                
  
    context = {
        'usuarioAtual': instUser,
        'funcionarioAtual':instFuncionario,
        'multiValoresAtual':instMulti
               
    }
    return render(request,"crufunc/alterar_funcionario.html", context)

# views para cliente

# views para venda

@login_required
def venda(request):
    Produtos = Produto.objects.all()
    return render(request,"cruvenda/venda.html", {'Produto': Produtos})


@login_required
def lista_venda(request):
    Produtos = Produto.objects.all()
    return render(request,"cruvenda/lista_venda.html", {'Produto': Produtos})