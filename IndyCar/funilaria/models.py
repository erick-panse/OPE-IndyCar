from django.db import models

# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    email = models.EmailField(max_length=60)
    #empresa = models.CharField(max_length=60)

class Cliente(Customer):
    cpf = models.CharField(max_length=9,primary_key=True)

class Empresa(Customer):
    cnpj = models.CharField(max_length=14,primary_key=True)



