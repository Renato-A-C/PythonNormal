from django.db import models
from django.contrib.postgres.functions import TransactionNow
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Produto(models.Model):
    nomeProduto = models.CharField(db_column='nomeProduto', max_length = 50, blank=True)
    dataCadastro = models.DateField(auto_now_add=TransactionNow(), blank=True)
    precoProduto = models.FloatField(db_column = 'precoProduto', blank= True)
    quantidadeProduto = models.BigIntegerField(db_column='quantidadeProduto', blank=True, default=1)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    def __str__(self):
        return str(self.nomeProduto)

class Funcionario(models.Model):
    
    nomeFuncionario = models.CharField(max_length=30,blank = True)
    cpfFuncionario = models.IntegerField(blank =True)
    enderecoFuncionario = models.CharField(max_length=150,blank = True)
    def __str__(self):
        return str(self.nomeFuncionario)


class Cliente(models.Model):
    nomeCliente= models.CharField(db_column='nomeCliente', max_length=50, blank=False)
    cpf = models.CharField(db_column='cpfCliente', max_length=15, blank=True)
    cnpj = models.CharField(db_column='cnpjCliente', max_length=50, blank=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    def __str__(self):
        return str(self.nomeCliente)
    
class Venda(models.Model):
    precoTotal = models.FloatField()
    produtoId = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="listagemProduto")
    funcionarioId = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="listagemFuncionario")
    clienteId= models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="listagemCliente")
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    def __str__(self):
        return (f"{self.id} do {self.funcionarioId.nomeFuncionario} ")
 
 
 
 
class User(AbstractBaseUser):
    
    pass