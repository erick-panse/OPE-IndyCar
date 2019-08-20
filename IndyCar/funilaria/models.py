from django.db import models

# Create your models here.

class Customer(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=8)
    email = models.EmailField(max_length=60)
    telefone = models.CharField(max_length=9)

class Cliente(Customer):
    rg = models.CharField(max_length=9,primary_key=True)

class Empresa(Customer):
    cnpj = models.CharField(max_length=14,primary_key=True)
    empresa = models.CharField(max_length=60)

class Car(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    ano = models.CharField(max_length=4)
    placa = models.CharField(max_length=7)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    entrada = models.DateTimeField(auto_now_add=True, blank=False))
    finalizado = models.DateTimeField(auto_now_add=True, blank=False)



