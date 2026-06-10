#------------------------------------
#-----Criação de Models de receitas--
#------------------------------------

from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_recebimento = models.DateField()
    fonte = models.CharField(max_length=100)
    observacao = models.TextField()

    def __str__(self):
        return self.descricao