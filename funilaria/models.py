from django.db import models
from django.urls import reverse 
# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60,blank=True,null=True)
    endereco = models.CharField(max_length=10,blank=True,null=True)
    bairro = models.CharField(max_length=8,blank=True,null=True)
    email = models.EmailField(max_length=60)
    telefone = models.IntegerField(default=000000000)
    marca_veiculo = models.CharField(max_length=10,blank=True,null=True)
    modelo_veiculo = models.CharField(max_length=20,blank=True,null=True)
    cor_veiculo = models.CharField(max_length=10,blank=True,null=True)
    ano_veiculo = models.SmallIntegerField(default=0000)
    placa_veiculo = models.CharField(max_length=7,blank=True,null=True)
    cidade_veiculo = models.CharField(max_length=10,blank=True,null=True)
    estado_veiculo = models.CharField(max_length=2,blank=True,null=True)
    entrada_veiculo = models.DateField(auto_now=True)
    saida_veiculo = models.DateField(blank=True,null=True)


class Cliente(Customer):
    rg = models.IntegerField()

    def get_editar_cliente(self):
        return reverse('editar_cliente',kwargs={'id':self.id})
    def get_del_cliente(self):
        return reverse('deletar_cliente',kwargs={'id':self.id})


class Empresa(Customer):
    cnpj = models.CharField(max_length=14)

    def get_editar_empresa(self):
        return reverse('editar_empresa',kwargs={'id':self.id})
    def get_del_empresa(self):
        return reverse('deletar_empresa',kwargs={'id':self.id})





