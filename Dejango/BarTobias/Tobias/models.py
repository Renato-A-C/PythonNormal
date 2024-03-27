from django.db import models
from django.contrib.postgres.functions import TransactionNow
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Produto(models.Model):
    Nome_do_produto = models.CharField(db_column='nomeProduto', max_length = 30, blank=True)
    dataCadastro = models.DateField(auto_now_add=TransactionNow(), blank=True)
    Descricao_do_Produto = models.CharField(db_column= 'DescProduto', max_length = 1000, blank = True)
    Preco_do_produto = models.FloatField(db_column = 'Preco', blank= True, default=1)
    Numero_de_Nota_Fiscal = models.CharField(db_column= 'NumNotaFiscal', max_length = 1000,blank = True)
    Quantidade_de_Produtos = models.BigIntegerField(db_column='Qtd', blank=True, default=1)

class Cliente(models.Model):
    nome= models.CharField(db_column='nomeCliente', max_length=50, blank=False)
    cpf = models.CharField(db_column='cpfCliente', max_length=15, blank=True)
    cnpj = models.CharField(db_column='cnpjCliente', max_length=50, blank=True)

class User(AbstractBaseUser):
    pass