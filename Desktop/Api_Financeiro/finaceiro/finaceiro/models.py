from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_recebimento = models.DateField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
