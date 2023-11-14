from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pagina_produtos(request):
    return HttpResponse('Página de produtos')

def celulares(request):
    return HttpResponse('Página de celulares')
