from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
from .models import Produto
import io
from reportlab.pdfgen import canvas
# Create your views here.
def index(request):
    return render(request,"index.html")

def listagem(request):
    novoItem = Produto()
    novoItem.nome=request.POST.get("nome")
    novoItem.email=request.POST.get("email")
    novoItem.save()

    produtos ={
        'produtos' : Produto.objects.all(),
    }
    return render(request,"listagem.html", produtos)

def cad(request):
    return render(request,"cad.html")