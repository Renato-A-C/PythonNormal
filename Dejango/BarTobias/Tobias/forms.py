from django import forms
from django.forms import Form, ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'  
        labels = {
            
            
        }
