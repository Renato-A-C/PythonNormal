from django import forms
from django.forms import Form, ModelForm
from .models import Produto, Cliente, Venda, Funcionario, LinkUser, CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  

        
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'  

        
class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'  

        
        
class CriadorDeConta(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LinkUserForm(ModelForm):
    class Meta:
        model = LinkUser
        fields = '__all__'  

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']