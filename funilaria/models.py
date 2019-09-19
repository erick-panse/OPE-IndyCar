from django.db import models
from django.urls import reverse 
# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome


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

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Customer,on_delete=models.PROTECT)
    marca_veiculo = models.CharField(max_length=10)
    modelo_veiculo = models.CharField(max_length=20)
    cor_veiculo = models.CharField(max_length=10)
    ano_veiculo = models.SmallIntegerField()
    placa_veiculo = models.CharField(max_length=7)
    cidade_veiculo = models.CharField(max_length=10)
    estado_veiculo = models.CharField(max_length=2)
    reparos_necessarios = models.TextField(max_length=200)
    prazo_entrega = models.DateField(null=True)
    entrada = models.DateField(auto_now_add=True, blank=True,null=True)
    finalizado = models.BooleanField(default=False,blank=True)

    def get_editar_ordem(self):
        return reverse('editar_ordem',kwargs={'id':self.id})
    def get_del_ordem(self):
        return reverse('deletar_ordem',kwargs={'id':self.id})

    def __str__(self):
        status_finalizado = "finalizado" if self.finalizado else "não finalizado"
        return "OS do cliente: "+str(self.cliente.nome)+" | "+status_finalizado

#TALVEZ ESSA CLASSE SEJA INÚTIL PQ O VALOR JA EXISTE NA ORDEM DE SERVIÇO
class Orcamento(models.Model):
    ordem_servico = models.ForeignKey(OrdemDeServico,on_delete=models.PROTECT,blank=True,null=True)
    quantidade = models.IntegerField()
    #QUANTIDADE DE Q ???????????
    pecas = models.TextField(max_length=200)
    servicos = models.TextField(max_length=500)
    valor_mao_de_obra = models.FloatField()
    previsao_entrega = models.DateField()
    data_saida = models.DateField()
    total_a_pagar = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return "orçamento | "+str(self.valor_mao_de_obra)
