from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.forms import formset_factory
from django.utils import timezone
from .models import Produto, Venda, Funcionario, Funcionario1, Funcionario2, ItemVenda, Cliente
from .forms import ProdutoForm,  VendaForm, FuncionarioForm, Funcionario1Form, Funcionario2Form, ClienteForm, ItemVendaForm, ItemVendaFormSet
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

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
            print("funciounou")
            try:
                print(f"salvo ")
                form.save()
                
                return redirect('lista_produto')
                
            except:
                pass
    else:
        form = ProdutoForm()
        print("não funfo")
    context= {
        'form':form,
        'func':Funcionario.objects.all()
    }
     
    return render(request,"cruproduto/criar_Produto.html", context)

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
    funcionario = Funcionario.objects.all()
    return render(request,"crufunc/lista_funcionario.html", {'Funcionario': funcionario})

@login_required
def cad_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        func1 = Funcionario1Form(request.POST)
        func2 = Funcionario2Form(request.POST)
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
        form = FuncionarioForm()
        func1 = Funcionario1Form()
        func2 = Funcionario2Form()
    context = {
        'form':form,
        'func1':func1,
        'func2':func2
    }
        
    return render(request,"registration/cad_funcionario.html", context)

@login_required
def alterar_funcionario(request, id):
    modeloUser = Funcionario.objects.get(id=id)
    linhaFuncionario = Funcionario1.objects.get(autor=modeloUser.id)
    print(f" aaaaa {linhaFuncionario.id}")
    linhaMulti= Funcionario2.objects.get(funcionario=linhaFuncionario.id)
    print(f" aaaaa {linhaMulti.id}")
    print(f" aaaaa {modeloUser.nome}")
    if request.method == "POST":
        modeloUser.nome = request.POST.get('nome')
        linhaFuncionario.nomeFuncionario = request.POST.get('nomeFuncionario')
        linhaFuncionario.cpfFuncionario = request.POST.get('cpfFuncionario')
        linhaFuncionario.enderecoFuncionario = request.POST.get('enderecoFuncionario')
        linhaMulti.descricao = request.POST.get('descricao')
        modeloUser.save()
        linhaFuncionario.save()
        linhaMulti.save()
        return redirect('lista_funcionario')
    else:
        instUser = FuncionarioForm() 
        instFuncionario = Funcionario1Form()
        instMulti = Funcionario2Form()     
                                
  
    context = {
        'usuarioAtual': instUser,
        'funcionarioAtual':instFuncionario,
        'multiValoresAtual':instMulti
               
    }
    return render(request,"crufunc/alterar_funcionario.html", context)


@login_required
def deletar_funcionario(request,id):
    funcionario = Funcionario1.objects.get(id=id)
    try:
        funcionario.delete()
    except:
        pass
    return redirect('lista_funcionario')


"""
# views para venda
"""
@login_required
def venda(request):
    venda = Venda.objects.all()
    
    context={
        'Venda': venda
    }
    return render(request,"cruvenda/venda.html", context)


@login_required
def lista_venda(request):
    venda = Venda.objects.all()
    func = Funcionario.objects.all()
    context={
        'venda': venda,
        'funcionario':func
    }
    return render(request,"cruvenda/lista_venda.html",context)

@login_required
def criar_venda2(request):
    
    print("criação iniciada")

    venda1 = VendaForm(request.POST)
    venda1 = Venda.objects.create()
    venda1.save()
    print(venda1.id)

    return redirect(f'criar_venda/{venda1.id}')
    
"""
    funcionarioId = models.ForeignKey(Funcionario1, on_delete=models.PROTECT, related_name="listagemFuncionario",)
    clienteId= models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="listagemCliente", )
    dataVenda = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
"""
@login_required
def addp(request,id):
    venda1 = Venda.objects.get(id=id)
    venda2 = ItemVenda.objects.create(venda = venda1)
    venda2.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
"""
    funcionarioId = models.ForeignKey(Funcionario1, on_delete=models.PROTECT, related_name="listagemFuncionario",)
    clienteId= models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="listagemCliente", )
    dataVenda = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
"""
@login_required
def criar_venda(request, id):
    venda1 = Venda.objects.get(id=id)
    funcionario = Funcionario1.objects.all()
    produto = Produto.objects.all()
    venda2 = ItemVenda.objects.filter(venda=id)
    print(ItemVenda.objects.count())

    if request.method == "POST":
        # = request.POST.get('')
        funcI = request.POST.get('funcionarioId')
        func = Funcionario1.objects.get(id=funcI)
        venda1.funcionarioId = func
        cliE = request.POST.get('clienteId')
        cli = Cliente.objects.get(id=cliE)
        venda1.clienteId = cli
        venda1.dataVenda = timezone.now()
        
        venda1.save()
        print("post validado")

        for key, value in request.POST.items():
            if key.startswith('quantidade_'):
                itemvenda_id = int(key.split('_')[1])
                itemvenda = ItemVenda.objects.get(id=itemvenda_id)
                itemvenda.quantidade = value
                itemvenda.save()
                print(f"quantidade feita {value}")
            elif key.startswith('produtoId_'):
                itemvenda_id = int(key.split('_')[1])
                itemvenda = ItemVenda.objects.get(id=itemvenda_id)
                print(f"valor {value}")
                produto_id = int(value)  # Supondo que o valor enviado seja o ID do produto
                produto1 = Produto.objects.get(id=produto_id)
                itemvenda.produtoId = produto1
                itemvenda.save()
                print('funcionou')
        print("aaaaaa")
        return redirect('venda')
        
    context = {
        'venda':venda1,
        'Funcionario':funcionario,
        'Produto': produto,
        'LProduto':ItemVenda.objects.filter(venda=id),
        'Cliente': Cliente.objects.all(),
       
    }
    return render(request, f'cruvenda/criar_venda.html', context)

"""
@login_required
def criar_venda(request):
    if request.method == "POST":
        pedido = Produto.objects.create(funcionario=Funcionario)
        produto = Produto.objects.get(id=1)
        
        quantidade = 2
        item = ItemVenda.objects.create(produtoId=produto, quantidade=quantidade)
        venda1 = VendaForm(request.POST)
        venda2 = ItemVendaForm(request.POST)
        item_venda_forms = [ItemVendaForm(request.POST, prefix=str(i)) for i in range(1, len(request.POST))]
        produto = ItemVenda.objects.filter(venda=Venda)
        print("ate aqui sim")
        if venda1.is_valid() and all(item_venda_form.is_valid() for item_venda_form in item_venda_forms):
            print("aaaaaa")
            try: 
                
                venda1.save()
                for item_venda_form in item_venda_forms:
                    item_venda = item_venda_form.save(commit=False)
                    item_venda.venda = venda1.id
                    item_venda.save()                
                #venda2.venda = venda1.id
                #venda2.save()
                s = 0
            except:
                pass
            return redirect('lista_venda')
    else:
        venda1 = VendaForm()
        venda2 = ItemVendaForm()
        item_venda_forms = [ItemVendaForm(prefix=str(i)) for i in range(1, 2)]
    produtos = Produto.objects.all()
    item_venda_formset = ItemVendaFormSet(initial=[{'produto': produto} for produto in produtos])
    context = {
        'venda': venda1,
        'lista': venda2,
        'Funcionario':Funcionario.objects.all(),
        'Produto': Produto.objects.all(),
        'Cliente': Cliente.objects.all(),
        'itemVenda': item_venda_formset
    }
    return render(request, 'cruvenda/criar_venda.html', context)



@login_required
def criar_venda(request):
    venda1 = VendaForm(request.POST)
    iv = ItemVendaForm(request.POST)
    produto = Produto.objects.all()
    funcionario = Funcionario1.objects.all()
    cliente = Cliente.objects.all()
    if venda1.is_valid() and iv.is_valid():
        print("aaaaaa")
        venda1.funcionarioId = funcionario.id
        venda1.save()
        
        item.venda = venda1.id
        item.save()
        itens = produto.save(commit=False)
        itensListados = []
        for item in itens.itens.all():
            novoItensListados = ItemVenda(nome= item.nomeProduto , quantidade = item.quantidadeProduto)
            itensListados.append(novoItensListados)
            
        ItemVenda.objects.bulk_create(itensListados)
        return redirect('lista_venda')
          # Redirecionar para a página de sucesso
    else:
        print("nao funcionou")
    context={
        
        'Produto': produto,
        'Funcionario':funcionario,
        'Cliente': cliente
    }

    return render(request, 'cruvenda/criar_venda.html', context)
"""

@login_required
def deletar_venda(request):
    venda = Venda.objects.get(id=id)
    venda.excluido = True
    venda.save()
    return redirect('lista_venda')

"""
Views para cliente
"""
@login_required
def lista_cliente(request):
    cliente = Cliente.objects.all()
    context = {
        'cliente': cliente
    }
    return render(request,"crucliente/lista_cliente.html", context)

@login_required
def alterar_cliente(request):
    cliente = Cliente.objects.all()
    context = {
        'cliente': cliente
    }
    return render(request,"crucliente/alterar_cliente.html", context)

@login_required
def deletar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cliente.excluido = True
    cliente.save()
    return redirect('lista_cliente')


# Views adicionais






class relatorio_pdf(View):
    def get(self, request, *args, **kwargs):
        # Inicialize o objeto Canvas
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
        c = canvas.Canvas(response, pagesize=A4)

        # Defina as dimensões dos retângulos
        largura = A4[0] - 100  # 100 é uma margem de 50 unidades em cada lado
        altura_pagina = A4[1]
        altura_superior = altura_pagina * 0.1
        altura_inferior = altura_pagina * 0.8

        # Desenhe os retângulos
        c.rect(50, altura_pagina - altura_superior - 50, largura, altura_superior)
        c.rect(50, 50, largura, altura_inferior)

        # Desenhe a estrutura da tabela de vendas no segundo quadrado
        margem_esquerda = 70
        margem_superior = 70
        largura_coluna = (largura - margem_esquerda * 2) / 5
        altura_linha = 20

        # Cabeçalhos da tabela
        cabecalhos = ["Item", "Nome", "Quantidade", "Preço Unitário", "Preço Total"]
        tamanhos_colunas = [30, 180, 65, 80, 100]  # Tamanhos fixos para cada coluna
        for i, (cabecalho, tamanho_coluna) in enumerate(zip(cabecalhos, tamanhos_colunas)):
            c.drawString(margem_esquerda + sum(tamanhos_colunas[:i]), altura_pagina - altura_superior - margem_superior, cabecalho)

            # Desenhe as linhas verticais entre as colunas
            if i > 0:
                c.line(margem_esquerda + sum(tamanhos_colunas[:i]), altura_pagina - altura_superior - margem_superior,
                       margem_esquerda + sum(tamanhos_colunas[:i]), altura_superior + margem_superior)

        # Dados da tabela de vendas (exemplo)
        produtos_venda = [
            {"nome": "Produto 1", "quantidade": 2, "preco_unitario": 10, "preco_total": 20},
            {"nome": "Produto 2", "quantidade": 1, "preco_unitario": 15, "preco_total": 15},
            {"nome": "Produto 3", "quantidade": 3, "preco_unitario": 8, "preco_total": 24},
        ]

        # Desenhe os produtos na tabela
        for i, produto in enumerate(produtos_venda):
            linha = margem_superior + altura_linha * (i + 2)
            c.drawString(margem_esquerda, altura_pagina - altura_superior - linha, str(i + 1))  # Número do item
            c.drawString(margem_esquerda + tamanhos_colunas[0], altura_pagina - altura_superior - linha, produto["nome"])
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1], altura_pagina - altura_superior - linha, str(produto["quantidade"]))
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1] + tamanhos_colunas[2], altura_pagina - altura_superior - linha, str(produto["preco_unitario"]))
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1] + tamanhos_colunas[2] + tamanhos_colunas[3], altura_pagina - altura_superior - linha, str(produto["preco_total"]))

            # Desenhe as linhas horizontais entre as linhas da tabela
            c.line(margem_esquerda, altura_pagina - altura_superior - (linha + altura_linha),
                   margem_esquerda + sum(tamanhos_colunas), altura_pagina - altura_superior - (linha + altura_linha))

        # Encerre o documento PDF
        c.showPage()
        c.save()

        return response
    
"""
class GerarPDF(View):
    def get(self, request, *args, **kwargs):
        # Inicialize o objeto Canvas
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
        c = canvas.Canvas(response, pagesize=A4)

        # Defina as dimensões dos retângulos
        largura = A4[0] - 100  # 100 é uma margem de 50 unidades em cada lado
        altura_pagina = A4[1]
        altura_superior = altura_pagina * 0.1
        altura_inferior = altura_pagina * 0.8

        # Desenhe os retângulos
        c.rect(50, altura_pagina - altura_superior - 50, largura, altura_superior)
        c.rect(50, 50, largura, altura_inferior)

        # Adicione o nome do usuário e do cliente
        usuario = request.user.username
        nome_cliente = "Nome do Cliente"  # Substitua pelo nome do cliente
        c.drawString(100, altura_pagina - 60, f"Usuário: {usuario}")
        c.drawString(100, altura_pagina - 80, f"Cliente: {nome_cliente}")

        # Desenhe a estrutura da tabela de vendas no segundo quadrado
        margem_esquerda = 70
        margem_superior = 70
        largura_coluna = (largura - margem_esquerda * 2) / 5
        altura_linha = 20

        # Cabeçalhos da tabela
        cabecalhos = ["Item", "Nome do Produto", "Quantidade", "Preço Unitário", "Preço Total"]
        tamanhos_colunas = [30, 180, 65, 80, 100]  # Tamanhos fixos para cada coluna
        for i, (cabecalho, tamanho_coluna) in enumerate(zip(cabecalhos, tamanhos_colunas)):
            c.drawString(margem_esquerda + sum(tamanhos_colunas[:i]), altura_pagina - altura_superior - margem_superior, cabecalho)

            # Desenhe as linhas verticais entre as colunas
            if i > 0:
                c.line(margem_esquerda + sum(tamanhos_colunas[:i]), altura_pagina - altura_superior - margem_superior,
                       margem_esquerda + sum(tamanhos_colunas[:i]), altura_superior + margem_superior)

        # Recuperar os dados da tabela listaDeProdutos
        produtos = ListaDeProdutos.objects.all()

        # Desenhe os produtos na tabela
        valor_total = 0
        for i, produto in enumerate(produtos):
            linha = margem_superior + altura_linha * (i + 2)
            c.drawString(margem_esquerda, altura_pagina - altura_superior - linha, str(i + 1))  # Número do item
            c.drawString(margem_esquerda + tamanhos_colunas[0], altura_pagina - altura_superior - linha, produto.nome_produto)
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1], altura_pagina - altura_superior - linha, str(produto.quantidade))
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1] + tamanhos_colunas[2], altura_pagina - altura_superior - linha, str(produto.preco_unitario))
            preco_total = produto.quantidade * produto.preco_unitario
            c.drawString(margem_esquerda + tamanhos_colunas[0] + tamanhos_colunas[1] + tamanhos_colunas[2] + tamanhos_colunas[3], altura_pagina - altura_superior - linha, str(preco_total))
            valor_total += preco_total

            # Desenhe as linhas horizontais entre as linhas da tabela
            c.line(margem_esquerda, altura_pagina - altura_superior - (linha + altura_linha),
                   margem_esquerda + sum(tamanhos_colunas), altura_pagina - altura_superior - (linha + altura_linha))
"""