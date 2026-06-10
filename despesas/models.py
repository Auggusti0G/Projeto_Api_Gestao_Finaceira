#----------------------------------------
#------Models de APP despesas Criado-----
#----------------------------------------

from django.db import models

class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    tipo = models.CharField(max_length=50)
    observacao = models.TextField()

    def __str__(self):
        return self.descricao