from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request ,'core/home.html')

def pagina1(request):
    return render(request ,'core/home.html')

def pagina2(request):
    return render(request ,'core/home.html')