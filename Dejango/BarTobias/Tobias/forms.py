from django import forms
from django.forms import Form, ModelForm, inlineformset_factory, modelformset_factory
from .models import Produto, Venda, Funcionario1, Funcionario2, Funcionario, Cliente, ItemVenda
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
import re
CustomUser = get_user_model()



def validar_cpf(value):
    cpf = re.sub(r'[^0-9]', '', value)  # Remove caracteres não numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        raise forms.ValidationError("CPF deve conter 11 dígitos numéricos.")
    if cpf == cpf[0] * 11:
        raise forms.ValidationError("CPF inválido.")
    for i in range(9, 11):
        soma = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise forms.ValidationError("CPF inválido.")
    return value

class FuncionarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    cpf = forms.CharField(max_length=14, required=True, validators=[validar_cpf])

    class Meta:
        model = Funcionario
        fields = ['email', 'nome', 'sobreNome', 'cpf']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Funcionario1Form(ModelForm):
    class Meta:
        model = Funcionario1
        fields = ['nomeFuncionario', 'enderecoFuncionario']

class Funcionario2Form(ModelForm):
    class Meta:
        model = Funcionario2
        fields = ['descricao']
        
        
        
                
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(max_length=14, required=True, validators=[validar_cpf])
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