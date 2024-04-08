from django.db import models
from django.contrib.postgres.functions import TransactionNow
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Produto(models.Model):
    nomeProduto = models.CharField(db_column='nomeProduto', max_length = 50, blank=True)
    dataCadastro = models.DateField(auto_now_add=TransactionNow(), blank=True)
    precoProduto = models.FloatField(db_column = 'precoProduto', blank= True)
    quantidadeProduto = models.BigIntegerField(db_column='quantidadeProduto', blank=True, default=1)

class Cliente(models.Model):
    nome= models.CharField(db_column='nomeCliente', max_length=50, blank=False)
    cpf = models.CharField(db_column='cpfCliente', max_length=15, blank=True)
    cnpj = models.CharField(db_column='cnpjCliente', max_length=50, blank=True)

class User(AbstractBaseUser):
    
    pass