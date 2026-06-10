#-------------------------------------------
#----Craiação de models do APP categorias---
#-------------------------------------------


from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome