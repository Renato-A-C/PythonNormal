from django.db import models
from django.conf import settings
from django.contrib.postgres.functions import TransactionNow
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
CustomUser = get_user_model()
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
    autor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
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
 
class LinkUser(models.Model):
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    

    
