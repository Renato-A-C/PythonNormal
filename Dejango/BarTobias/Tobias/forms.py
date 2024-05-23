from django import forms
from django.forms import Form, ModelForm, inlineformset_factory, modelformset_factory
from .models import Produto, Venda, Funcionario1, Funcionario2, Funcionario, Cliente, ItemVenda
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
CustomUser = get_user_model()



class FuncionarioForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = Funcionario
        fields = ['email', 'nome', 'sobreNome', 'password1', 'password2']

class Funcionario1Form(ModelForm):
    class Meta:
        model = Funcionario1
        fields = ['nomeFuncionario', 'cpfFuncionario', 'enderecoFuncionario']
        
class Funcionario2Form(ModelForm):
    class Meta:
        model = Funcionario2
        fields = ['descricao']  
        
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['funcionarioId', 'clienteId']

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produtoId', 'quantidade']
        
ItemVendaFormSet = inlineformset_factory(
    Venda,  # Modelo pai
    ItemVenda,  # Modelo filho
    form=ItemVendaForm,  # Formulário para cada item de venda
    extra=1,  # Número inicial de formulários a serem exibidos na template
    can_delete=True,  # Permitir excluir itens de venda
)