from django.db import models
from django.urls import reverse 
from model_utils.managers import InheritanceManager
from datetime import datetime
from django.utils import timezone
# Create your models here.
"""
#n precisa mais já q ta salvando o cpf e cnpj com a mascara
def formatarCpf(cpf):
    cpf=str(cpf)
    f=""
    for i in range(len(cpf)):
        if i!=0 and i%3==0 and i+3<=len(cpf):
            f+='.'+cpf[i]
        elif i==9:
            f+='/'+cpf[i]
        else:
            f+=cpf[i]
    return f

def formatarCnpj(cnpj):
    cnpj=str(cnpj)
    f=""
    for i in range(len(cnpj)):
        if i==2 or i==5:
            f+='.'+cnpj[i]
        elif i==8:
            f+='/'+cnpj[i]
        elif i==12:
            f+='-'+cnpj[i]
        else:
            f+=cnpj[i]
    return f
"""

class Estado(models.Model):
    sigla = models.CharField(max_length=2,unique=True)
    nome = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.sigla+" - "+self.nome

ESTADO_CARRO= [
    ('AC', 'Acre'),    
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')]

for i in ESTADO_CARRO:
    try:
        e = Estado(sigla=i[0],nome=i[1])
        e.save()
    except:
        pass

class Customer(models.Model):
    objects = InheritanceManager()
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    telefone = models.CharField(max_length=15)

class Cliente(Customer):
    cpf = models.CharField(unique=True,max_length=14)

    def get_editar_cliente(self):
        return reverse('editar_cliente',kwargs={'id':self.id})
    def get_del_cliente(self):
        return reverse('deletar_cliente',kwargs={'id':self.id})

    def __str__(self):
        return self.nome +" | "+self.cpf


class Empresa(Customer):
    cnpj = models.CharField(unique=True,max_length=18)

    def get_editar_empresa(self):
        return reverse('editar_empresa',kwargs={'id':self.id})
    def get_del_empresa(self):
        return reverse('deletar_empresa',kwargs={'id':self.id})

    def __str__(self):
        return self.nome +" | "+self.cnpj

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Customer,on_delete=models.PROTECT)
    marca_veiculo = models.CharField(max_length=30)
    modelo_veiculo = models.CharField(max_length=30)
    cor_veiculo = models.CharField(max_length=30)
    ano_veiculo = models.SmallIntegerField()
    placa_veiculo = models.CharField(unique=True,max_length=8)
    cidade_veiculo = models.CharField(max_length=30)
    estado_veiculo = models.ForeignKey(Estado,on_delete=models.PROTECT)
    reparos_necessarios = models.TextField(max_length=200)
    entrada = models.DateField(auto_now_add=True,blank=True)
    prazo_entrega = models.DateField(default=timezone.now)
    data_finalizacao = models.DateField(blank=True,null=True)

    def get_editar_ordem(self):
        return reverse('editar_ordem',kwargs={'id':self.id})
    def get_del_ordem(self):
        return reverse('deletar_ordem',kwargs={'id':self.id})

    def __str__(self):
        return "OS do cliente: "+str(self.cliente.nome)

    @property
    def status(self):
        if self.data_finalizacao:
            return True
        return False

    @property
    def data_entrega(self):
        return self.prazo_entrega.strftime("%d/%m/%Y")


class Material(models.Model):
    descricao = models.TextField(max_length=200)
    quantidade_estoque = models.IntegerField()
    valor = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):
        return str(self.descricao)

    def get_editar_material(self):
        return reverse('editar_material',kwargs={'id':self.id})
    
    def get_del_material(self):
        return reverse('deletar_material',kwargs={'id':self.id})

    def get_add_carrinho(self):
        return reverse("add_no_carrinho", kwargs={'id': self.id})

    def get_tirar_carrinho(self):
        return reverse("tirar_do_carrinho", kwargs={'id': self.id})

    def get_add_carrinho2(self):
        return reverse("add_no_carrinho2", kwargs={'id': self.id})

    def get_tirar_carrinho2(self):
        return reverse("tirar_do_carrinho2", kwargs={'id': self.id})


from django.conf import settings
class EstoqueMaximoException(Exception):
    def __init__(self, message):
        super().__init__(message)
         

class ItemCarrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.material.descricao+" x"+str(self.quantidade)
    
    @property
    def total(self):
        return self.material.valor*self.quantidade

    def add(self,qtd=1):
        m=self.material
        if m.quantidade_estoque>=qtd:
            self.quantidade+=qtd
            m.quantidade_estoque-=qtd
            m.save()
            self.material=m
            return True
        else:
            raise EstoqueMaximoException('Limite do estoque atingido')
            return False


    def remover(self):
        m=self.material
        if self.quantidade>0:
            m.quantidade_estoque+=1
            self.quantidade-=1
            m.save()
            self.material=m



class Carrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemCarrinho)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return str('Carrinho de: '+str(self.usuario))

    def add_orcamento(self):
        return reverse('orcamento',kwargs={'id':self.id})

    @property
    def total(self):
        t=0
        for i in self.itens.all():
            t+=i.total
        return t



class Orcamento(models.Model):
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    ordem_de_servico = models.ForeignKey(OrdemDeServico,on_delete=models.PROTECT)
    carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE)
    servicos = models.TextField(max_length=500)
    valor_mao_de_obra = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    previsao_entrega = models.DateField()
    data_saida = models.DateField(blank=True,null=True)
    total_a_pagar = models.DecimalField(decimal_places=2,max_digits=8,default=0)

    def __str__(self):
        return self.servicos+" | "+str(self.total_a_pagar)

    def get_editar_orcamento(self):
        return reverse('editar_orcamento',kwargs={'id':self.id})
    
    def get_del_orcamento(self):
        return reverse('deletar_orcamento',kwargs={'id':self.id})

    @property
    def resumo(self):
        res=[]
        if self.carrinho:
            for i in self.carrinho.itens.all():
                res.append(i.material.descricao+' x'+str(i.quantidade))
            return res
        return 'sem carrinho'

    @property
    def total(self):
        return self.valor_mao_de_obra+self.carrinho.total


    @property
    def status(self):
        if self.data_saida:
            return True
        return False

    def save(self, force_insert=False, force_update=False):
        self.total_a_pagar = self.total
        super(Orcamento, self).save(force_insert, force_update)
################################################################################################
