from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.TextField()
    dataCadastro = models.DateField(auto_now_add=True, null=True)
    email = models.EmailField(blank=True,null=True)
    
    def __str__(self):
        return self.nome 