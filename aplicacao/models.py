from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    telefone = models.CharField(max_length=25, null=True, blank=True)
    rua = models.CharField(max_length=25, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=50, null=True, blank=True)
    cliente = models.OneToOneFiel(User, on_delete=models.CASCADE)

    def __str__(self_):
        return f'Pefil de {sel.cliente.username}'

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    itemVenda = models.ManyToManyFIeld(Venda)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data = models.DateField(auto_now_add=True)
    clinte = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self_):
        return self.data

class itemVenda(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10,null=true, blank=True)
    qtde = models.IntegerField(nuel=True,blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.CharField(max_length=100, null=True, blank=True)
