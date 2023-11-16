from django.shortcuts import render

def index(request):
    return render(request, 'clientes/index.html')

def emails(request):
    return render(request, 'clientes/email.html')
