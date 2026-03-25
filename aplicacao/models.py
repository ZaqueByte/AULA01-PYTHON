from django.db import models
from django.contrib.auth.models import User 


class Perfil (models.Model):
    telefone = models.CharField(max_length=10, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    numero = models.PositiveIntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=100, null=True, blank=True)
    cliente = models.OneToOneField(User, on_delete = models.CASCADE)

 
    def __str__(self):
     return f'Perfil de {self.cliente.username}'



class Venda(models.Model):
    data = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(User,on_delete = models.CASCADE)
 
    def __str__(self):
        return self.data
    
class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    itemVenda = models.ManyToManyField(Venda)

    def __str__(self):
        return self.nome



class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.produto.nome}'
    

