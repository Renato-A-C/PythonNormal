from django.db import models
from django.conf import settings
from django.contrib.postgres.functions import TransactionNow
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
# Create your models here.

class FuncionarioManager(BaseUserManager):
    def create_user(self, email, nome, sobreNome, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, sobreNome=sobreNome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, sobreNome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, nome, sobreNome, password, **extra_fields)

class Funcionario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    sobreNome = models.CharField(max_length=30)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = FuncionarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobreNome']

    def __str__(self):
        return str(self.nome)
    

class Funcionario1(models.Model):
    autor = models.OneToOneField(Funcionario,on_delete=models.CASCADE)
    nomeFuncionario = models.CharField(max_length=30,blank = True)
    cpfFuncionario = models.IntegerField(blank =True)
    enderecoFuncionario = models.CharField(max_length=150,blank = True)
    
    def __str__(self):
        return str(self.nomeFuncionario)

class Funcionario2(models.Model):
    funcionarioId = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="idFuncionario",)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return str(self.funcionario)    
    
Funcionario = get_user_model()
class Produto(models.Model):
    nomeProduto = models.CharField(db_column='nomeProduto', max_length = 50, blank=True)
    cadastro= models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="produtoFuncionario", default=1)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    dataAlteracao = models.DateTimeField(blank=True)
    precoProduto = models.FloatField(db_column = 'precoProduto', blank= True)
    quantidadeProduto = models.BigIntegerField(db_column='quantidadeProduto', blank=True, default=1)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
 
    def __str__(self):
        return str(self.nomeProduto)


class Cliente(models.Model):
    nomeCliente= models.CharField(db_column='nomeCliente', max_length=50, blank=False)
    cadastro= models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="cadastroFuncionario", default=1)
    cpf = models.CharField(db_column='cpfCliente', max_length=15, blank=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    def __str__(self):
        return str(self.nomeCliente)
  
class Venda(models.Model):
 
    funcionarioId = models.ForeignKey(Funcionario1, on_delete=models.PROTECT, related_name="listagemFuncionario",)
    clienteId= models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="listagemCliente", )
    dataVenda = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    precoTotal= models.FloatField()
    def __str__(self):
        return (f"{self.id} do {self.funcionarioId.nomeFuncionario}")
 
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produtoId = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="listagemProduto")
    quantidade = models.IntegerField()
    precoItem= models.FloatField()
    def __str__(self):
        return (f"{self.venda.id}, {self.produtoId}")

    
