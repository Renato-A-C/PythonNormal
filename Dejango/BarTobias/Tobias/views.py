from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.forms import formset_factory
from django.utils import timezone
from .models import Produto, Venda, Funcionario, Funcionario1, Funcionario2, ItemVenda, Cliente
from .forms import ProdutoForm,  VendaForm, FuncionarioForm, Funcionario1Form, Funcionario2Form, ClienteForm, ItemVendaForm, ItemVendaFormSet
from .utils import is_chefe, is_funcionario

import re
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
# -*- coding: utf-8 -*-

# Create your views here.
def home(request):

    return render(request,"home.html")

# views para produtos
# views para filtragem dos produtos
#  nome
@login_required
def lista_produto(request):
    Produtos = Produto.objects.all().order_by("nomeProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }    
    return render(request,"cruproduto/lista_produto.html", context)

@login_required
def lista_produtod(request):
    Produtos = Produto.objects.all().order_by("-nomeProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    
    return render(request,"cruproduto/lista_produto.html", context)

# preco
@login_required
def lista_produtopa(request):
    Produtos = Produto.objects.all().order_by("precoProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }

    return render(request,"cruproduto/lista_produto.html", context)

@login_required
def lista_produtopd(request):
    Produtos = Produto.objects.all().order_by("-precoProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)

# data
@login_required
def lista_produtoda(request): 
    Produtos = Produto.objects.all().order_by("dataAlteracao")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)

@login_required
def lista_produtodd(request):
    Produtos = Produto.objects.all().order_by("-dataAlteracao")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    

    return render(request,"cruproduto/lista_produto.html", context)

# quantidade
@login_required
def lista_produtoqa(request):
    Produtos = Produto.objects.all().order_by("quantidadeProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)

@login_required
def lista_produtoqd(request):
    Produtos = Produto.objects.all().order_by("-quantidadeProduto")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)
# id
@login_required
def lista_produtoia(request):
    Produtos = Produto.objects.all().order_by("id")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)

@login_required
def lista_produtoid(request):
    Produtos = Produto.objects.all().order_by("-id")

    context ={
        'Produto':Produtos,
        'func':Funcionario1.objects.all(),
    }
    return render(request,"cruproduto/lista_produto.html", context)

# resto do crud produto
@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            print("funciounou")
            try:
                print(f"salvo ")
                form.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
            except:
                pass
    else:
        form = ProdutoForm()
        print("não funfo")
        return render(request, 'cruproduto/lista_produto.html', {'form': form})

     

@login_required
def alterar_produto(request,id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        
     
        produto.nomeProduto = request.POST.get('nomeProduto')
        
        produto.precoProduto = request.POST.get('precoProduto')
      
        produto.quantidadeProduto = request.POST.get('quantidadeProduto')
        #momento = timezone.now()
        #produto.dataAlteracao = momento
        produto.save()
        
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        print("nao é post")
        return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def lancar_produto(request,id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        qtd = produto.quantidadeProduto
        print(qtd)

        produto.quantidadeProduto = produto.quantidadeProduto + int(request.POST.get('quantidadeProduto'))
        momento = timezone.now()
        produto.dataAlteracao = momento
        produto.save()
        print('produto lancado')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    else:
        print("nao é post")
        return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def deletar_produto(request,id):
    produto = Produto.objects.get(id=id)

    produto.excluido = True
    produto.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def consulta_produto(request):
    Produtos = Produto.objects.all()
    return render(request,"cruproduto/consulta_produto.html", {'Produto': Produtos})


"""
# views para funcionario
""" 

@login_required
def verif(request):
    grupo = Group.objects.get(id=1)
    permissoes = grupo.permissions.all()
    for permissao in permissoes:
        print(f'Permissão: {permissao.name} (codename: {permissao.codename})')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def promover(request,id):
    
    if not request.user.is_superuser:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    func = get_object_or_404(Funcionario, id=id)
    grupo = get_object_or_404(Group, id=1)
    func.groups.add(grupo)
    func.save()  # Salva a instância do usuário após a modificação
    
    return redirect("lista_funcionario")
    
@permission_required('Tobias.view_funcionario')
@login_required

def lista_funcionario(request):
    #funcionario = Funcionario.objects.all().order_by('nome')
    funcionario = Funcionario.objects.filter(excluido=False).order_by('nome')
    funcionario1 = Funcionario1.objects.all()
    desc = Funcionario2.objects.all()
    for funcionarios in funcionario:
        funcionarios.e_chefe = funcionarios.groups.filter(id=1).exists()
     
    context={
        'funcionario': funcionario,
        'funcionario1': funcionario1,
        'desc': desc,
        

    } 
    return render(request,"crufunc/lista_funcionario.html", context)

# Verifica se o usuário pertence ao grupo 'chefe'
@permission_required('Tobias.view_funcionario')
@login_required
def cad_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        func1_form = Funcionario1Form(request.POST)
        func2_form = Funcionario2Form(request.POST)
        if form.is_valid() and func1_form.is_valid() and func2_form.is_valid():
            user = form.save()
            func1 = func1_form.save(commit=False)
            func1.autor = user
            func1.save()
            func2 = func2_form.save(commit=False)
            func2.funcionarioId = user
            func2.save()

            # Verifica o grupo do usuário atual
            grupo_name = 'Funcionario'

            # Adiciona o usuário ao grupo correspondente
            try:
                grupo = Group.objects.get(name='Funcionario')
                user.groups.add(grupo)
            except Group.DoesNotExist:
                # Lidar com o caso em que o grupo não existe
                print("O grupo 'Funcionario' não existe.")
            except Exception as e:
                # Lidar com outros erros
                print(f"Erro ao adicionar usuário ao grupo: {e}")

            return redirect('lista_funcionario')
        else:
            print(form.errors, func1_form.errors, func2_form.errors)
    else:
        form = FuncionarioForm()
        func1_form = Funcionario1Form()
        func2_form = Funcionario2Form()

    context = {
        'form': form,
        'func1_form': func1_form,
        'func2_form': func2_form,
    }
    return render(request, "registration/cad_funcionario.html", context)

@login_required
def alterar_funcionario(request, id):
    modeloUser = Funcionario.objects.get(id=id)
    linhaFuncionario = Funcionario1.objects.get(autor=modeloUser.id)
    print(f" aaaaa {linhaFuncionario.id}")
    linhaMulti= Funcionario2.objects.filter(funcionarioId=modeloUser.id)
    
    print(f" aaaaa {modeloUser.nome}")
    if request.method == "POST":
        modeloUser.nome = request.POST.get('nome')
        modeloUser.sobreNome = request.POST.get('sobreNome')
        linhaFuncionario.nomeFuncionario = request.POST.get('nomeFuncionario')
        linhaFuncionario.cpfFuncionario = request.POST.get('cpf')
        linhaFuncionario.enderecoFuncionario = request.POST.get('enderecoFuncionario')
        
            
        
        modeloUser.save()
        linhaFuncionario.save()
        for i in linhaMulti:
            i.descricao = request.POST.get('descricao')
            i.save()
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
    funcionario = Funcionario.objects.get(id=id)
    funcionario.excluido = True
    funcionario.save()
    print("DELETADO")
        

    return redirect('lista_funcionario')


"""
# views para venda
"""
@login_required
def venda(request):
    venda = Venda.objects.all().order_by('-dataVenda')
    
    context={
        'Venda': venda
    }
    return render(request,"cruvenda/venda.html", context)

def detalhes_venda(request):
    venda_id = request.GET.get('venda_id')
    venda = Venda.objects.get(pk=venda_id)
    
    # Obtemos os dados diretamente da variável 'venda'
    funcionario_id = venda.funcionarioId.nomeFuncionario # Supondo que 'funcionarioId' seja uma ForeignKey
    data_venda = venda.dataVenda.strftime('%d/%m/%Y às %H:%M')# Converta para string no formato desejado

    response_data = {
        'funcionarioId': funcionario_id,
        'dataVenda': data_venda,
    }
    return JsonResponse(response_data)

def detalhes_produto(request):
    produto_id = request.GET.get('produto_id')
    produto = Produto.objects.get(pk=produto_id)
    
    # Obtemos os dados diretamente da variável 'venda'
    preco = produto.precoProduto # Supondo que 'funcionarioId' seja uma ForeignKey
    quantidadeRestante = produto.quantidadeProduto# Converta para string no formato desejado

    response_data = {
        'preco': preco,
        'quantidade': quantidadeRestante,
    }
    return JsonResponse(response_data)



@login_required
def criar_venda2(request):
    
    print("criação iniciada")

    venda1 = VendaForm(request.POST)
    venda1 = Venda.objects.create()
    venda1.save()
    print(venda1.id)

    return redirect(f'criar_venda/{venda1.id}')
    


@login_required
def criar_venda(request, id):
    venda1 = Venda.objects.get(id=id)
    funcionario = Funcionario1.objects.all()
    produto = Produto.objects.all()
    venda2 = ItemVenda.objects.filter(venda=id)
    qtdProdutoBanco  = Produto.objects.filter(quantidadeProduto__gt=0, excluido=False).count()
    maxqtd = ItemVenda.objects.filter(venda=id).count()
    print(ItemVenda.objects.count())

    if request.method == "POST":
        # = request.POST.get('')
        funcI = request.POST.get('funcionarioId')
        func = Funcionario1.objects.get(id=funcI)
        venda1.funcionarioId = func
        cliE = request.POST.get('clienteId')
        cli = Cliente.objects.get(id=cliE)
        venda1.clienteId = cli
        #venda1.dataVenda = timezone.now()
        venda1.save()
        print("post validado")

        for key, value in request.POST.items():
            if key.startswith('quantidade_'):
                itemvenda_id = int(key.split('_')[1])
                itemvenda = ItemVenda.objects.get(id=itemvenda_id)
                itemvenda.quantidade = value
                itemvenda.save()
                print(f"quantidade alocada foi {value}")
            elif key.startswith('produtoId_'):
                itemvenda_id = int(key.split('_')[1])
                itemvenda = ItemVenda.objects.get(id=itemvenda_id)
                
                produto_id = int(value)  # Supondo que o valor enviado seja o ID do produto
                produto1 = Produto.objects.get(id=produto_id)
                itemvenda.produtoId = produto1
                itemvenda.save()
                print('item corrigido')
                
        

        print("Aqui validou redirect")
        if "addpV2" in request.POST:
            v = Venda.objects.get(id=id)
 
            pTot=[]
            cont=0
            pTotal=0
            preco =0
            for i in venda2:
                p = i.quantidade * i.produtoId.precoProduto
                i.precoItem = p
                i.save()
                pTot.append(p)
                pTotal += p
                print(f"o preco armazenado aqui é {pTotal}")
                cont =+1
                venda1.precoTotal = pTotal
                venda1.save()
            novo = ItemVenda.objects.create(venda = v)
            novo.save()  
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            v = Venda.objects.get(id=id)
            pTot=[]
            cont=0
            pTotal=0
            preco =0
            for i in venda2:
                p = i.quantidade * i.produtoId.precoProduto
                i.precoItem = p
                i.save()
                pTot.append(p)
                pTotal += p
                print(f"o preco armazenado aqui é {pTotal}")
                cont =+1
                venda1.precoTotal = pTotal
                venda1.save()
            
            for index in ItemVenda.objects.filter(venda= venda1 ):
                prod = Produto.objects.get(id = index.produtoId.id)
                qtd = prod.quantidadeProduto 
                prod.quantidadeProduto = qtd - index.quantidade
                momento = timezone.now()
                prod.dataAlteracao = momento
                prod.save()
                print(f"{qtd-1}, {index.quantidade}")

            return redirect('venda')
            
    context = {
        'venda':venda1,
        'Funcionario':funcionario,
        'Produto': produto,
        'LProduto':ItemVenda.objects.filter(venda=id),
        'Cliente': Cliente.objects.all(),
        'qtd':qtdProdutoBanco,
        'max':maxqtd
    }
    return render(request, f'cruvenda/criar_venda.html', context)
"""
@login_required
def addp(request,id):
    print
"""
# Atualmente inutilizado
@login_required
def addpV2(request,id):
    venda1 = Venda.objects.get(id=id)
    venda2 = ItemVenda.objects.create(venda = venda1)
    venda2.save()
    for key, value in request.POST.items():
        if key.startswith('quantidade_'):
            itemvenda_id = int(key.split('_')[1])
            itemvenda = ItemVenda.objects.get(id=itemvenda_id)
            itemvenda.quantidade = value
            itemvenda.save()
            print(f"quantidade alocada foi {value}")
        elif key.startswith('produtoId_'):
            itemvenda_id = int(key.split('_')[1])
            itemvenda = ItemVenda.objects.get(id=itemvenda_id)
            produto_id = int(value)  # Supondo que o valor enviado seja o ID do produto
            produto1 = Produto.objects.get(id=produto_id)
            itemvenda.produtoId = produto1
            itemvenda.save()
            print('item corrigido') 
        itemvenda.tot = venda2.produtoId.precoProduto * venda2.quantidade
        print(f"{venda2.tot} o preco aq é")
        venda2.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

 
@login_required
def removep(request,id):
    venda1 = ItemVenda.objects.get(id=id)
    venda1.delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def exib_venda(request,id):
    
    venda = Venda.objects.get(id=id)
    item = ItemVenda.objects.filter(venda=id).order_by('produtoId')
    produto = Produto.objects.all()

    context={
        'Venda':venda,
        'Item':item
    } 
    return render(request,"cruvenda/exib_venda.html",context)


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
def criar_cliente(request):
    
    if request.method == "POST":
        print("request é post")
        cliente = ClienteForm(request.POST)
        if cliente.is_valid():
            print("até aqui tá funfando")
            try:
                print(f"salvo")
                cliente.save()
                return redirect("lista_cliente")
            except:
                pass
    else:
        cliente = ClienteForm()
        print("não funfo")
    
    context= {
        'cliente':cliente,
        'func':Funcionario.objects.all(),
        'funci':Funcionario1.objects.all()
    }
    return render(request,"crucliente/criar_cliente.html", context)

@login_required
def lista_cliente(request):
    cliente = Cliente.objects.all()
    context = {
        'cliente': cliente
    }
    return render(request,"crucliente/lista_cliente.html", context)

@login_required
def alterar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    print(f" aaaaa {cliente.id}")
    print(f" aaaaa {cliente.nomeCliente}")
    if request.method == "POST":
        cliente.nomeCliente = request.POST.get('nomeCliente')
        cliente.cpf = request.POST.get('cpf')
        cliente.save()
        print("Funciounou krai")
        return redirect(lista_cliente)
    else:
        print("Nao foi validado")
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
    """
    class Venda(models.Model):
 
    funcionarioId = models.ForeignKey(Funcionario1, on_delete=models.PROTECT, related_name="listagemFuncionario",)
    clienteId= models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="listagemCliente", )
    dataVenda = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    precoTotal= models.FloatField(default=0)
    def __str__(self):
        return f"{self.id} do {self.funcionarioId.nomeFuncionario}"
 
    """
def generate_items_pdf(request, id):
    venda  =Venda.objects.get(id=id)
    itens_venda = ItemVenda.objects.filter(venda=venda.id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (f'attachment; filename="itens_venda_{venda.id}.pdf"')

    dados = []

    #for item in itens:
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []  # Lista para armazenar os elementos do PDF
    
    styles = getSampleStyleSheet()
    style_title = styles['Title']  # Estilo para o título
    style_normal = styles['Normal']  # Estilo para o texto normal   
    
    data = [["Item", "Descrição", "Quantidade", "Valor Unitário", "Valor Total"]]
    for i, item in enumerate(itens_venda, start=1):
        # Adiciona cada item da venda à tabela
        data.append([
            str(i),
            item.produtoId.nomeProduto,
            str(item.quantidade),
            f"R$ {item.produtoId.precoProduto:.2f}",
            f"R$ {item.precoItem:.2f}"
        ])
    data.append([
        '',  # Coluna vazia para o índice
        '',  # Coluna vazia para a descrição
        '',  # Coluna vazia para a quantidade
        'Total',  # Texto 'Total'
        f"R$ {venda.precoTotal:.2f}"  # Valor total da venda
    ])
    data.append([
        '',  # Coluna vazia para o índice
        f'Funcionario: {venda.funcionarioId.nomeFuncionario} ',  # Coluna vazia para a descrição
        f'Cliente {venda.clienteId.nomeCliente}',  # Coluna vazia para a quantidade
          # Texto 'Total'
          # Valor total da venda
    ])
    table = Table(data, colWidths=[40, 200, 70, 90, 90])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Fundo do cabeçalho
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Cor do texto do cabeçalho
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento do texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento inferior do cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Fundo das linhas
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade da tabela
    ]))
    elements.append(table)  # Adiciona a tabela ao PDF

    doc.build(elements)  # Constrói o PDF com os elementos
    
    return response 

