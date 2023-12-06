from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    dataCadastro = models.DateField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.nome