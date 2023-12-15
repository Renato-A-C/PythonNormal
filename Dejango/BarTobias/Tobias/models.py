from django.db import models
from django.contrib.postgres.functions import TransactionNow
# Create your models here.
class Produto(models.Model):
    nome = models.CharField(db_column='nomeProduto', max_length = 30, blank=False)
    dataCadastro = models.DateField(auto_now_add=TransactionNow(), blank=True)
    DescProduto = models.TextField(db_column= 'DescProduto', max_length = 1000, blank = True)
    Preco = models.FloatField(db_column = 'Preco', blank= True, default=1)
    NumNotaFiscal = models.TextField(db_column= 'NumNotaFiscal', max_length = 1000,blank = True)
    QtdProduto = models.BigIntegerField(db_column='Qtd', blank=True, default=1)
    def __str__(self):
        return self.nome 


class Cliente(models.Model):
    nome= models.CharField(db_column='nomeCliente', max_length=50, blank=False)
    cpf = models.CharField(db_column='cpfCliente', max_length=15, blank=True)
    cnpj = models.CharField(db_column='cnpjCliente', max_length=50, blank=True)