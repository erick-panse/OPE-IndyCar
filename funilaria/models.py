from django.db import models
from django.urls import reverse 
# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    telefone = models.IntegerField()
    marca_veiculo = models.CharField(max_length=10)
    modelo_veiculo = models.CharField(max_length=20)
    cor_veiculo = models.CharField(max_length=10)
    ano_veiculo = models.SmallIntegerField()
    placa_veiculo = models.CharField(max_length=7)
    cidade_veiculo = models.CharField(max_length=10)
    estado_veiculo = models.CharField(max_length=2)


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

class Orcamento():
    quantidade = models.IntegerField()
    pecas = models.TextField(max_length=200)
    servicos = models.TextField(max_length=500)
    mao_de_obra = models.FloatField()
    previsao_entrega = models.DateField()
    data_saida = models.DateField()
    total_a_pagar = models.DecimalField()


class OrdemDeServico(Customer):
    reparos_necessarios = models.TextField(max_length=200)
    entrada = models.DateField()
    prazo_entrega = models.DateField()
    finalizado = models.DateField()
