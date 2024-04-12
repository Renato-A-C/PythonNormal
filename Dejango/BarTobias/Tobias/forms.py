from django import forms
from django.forms import Form, ModelForm
from .models import Produto, Cliente, Venda, Funcionario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  
        labels = {
        }
        
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  
        labels = {
        }

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'  
        labels = {
        }
        
class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'  
        labels = {
        }
