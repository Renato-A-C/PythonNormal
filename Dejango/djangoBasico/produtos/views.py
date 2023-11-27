from django.shortcuts import render
"""
Tem os recursos para fazer a exibição 
utilizando o html e css (templates)
"""

# Create your views here.
def index(request):
    # processamento, banco de dados
    idade = 15
    tipo = ''

    if idade < 12:
        tipo = 'Criança'
    elif idade >= 12 and idade <= 18:
        tipo = 'Adolescente'
    else:
        tipo = 'Adulto'

    context = {
        'nome': 'Jamilton Damasceno',
        'ultimo_acesso': '10/10/2030',
        'idade': 10,
        'tipo': tipo,
        'produtos': [
            {'nome': 'Notebook Acer', 'preco': '1.200,00'},
            {'nome': 'Iphone', 'preco': '2.200,00'},
            {'nome': 'Samsung', 'preco': '4.200,00'},
        ]
    }

    return render(request, 'index.html', context)

def celulares(request):
    return render(request, 'celulares.html')
