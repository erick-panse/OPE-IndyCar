from django.db import models

# Create your models here.
class Cliente(models.Model):
    cnpj_rg = models.CharField(max_length=60,primary_key=True)
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    empresa = models.CharField(max_length=60)




