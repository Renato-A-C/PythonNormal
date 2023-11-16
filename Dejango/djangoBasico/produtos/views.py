from django.shortcuts import render
"""
Tem os recursos para fazer a exibição 
utilizando o html e css (templates)
"""
from django.http import HttpResponse

# Create your views here.
def index(request):
    # procesamento banco de dados
    context = {
        'nome'='arroz'
    }
    return render(request, 'index.html')

def celulares(request):
    return render(request, 'celulares.html')
