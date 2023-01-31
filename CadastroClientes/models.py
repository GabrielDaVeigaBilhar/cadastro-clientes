from django.db import models

class Cliente(models.Model):
    ClienteId = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100,  unique=True)
    Telefone = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=100)
    CEP = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=100)