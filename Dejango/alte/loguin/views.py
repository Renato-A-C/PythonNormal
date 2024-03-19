from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request ,'home.html')

@login_required
def pagina1(request):
    return render(request ,'pagina1.html')

@login_required
def pagina2(request):
    return render(request ,'pagina2.html')