#----------------------------------------------
#----Criação do registro do app de despesas----
#----------------------------------------------

from django.contrib import admin
from .models import Despesa

admin.site.register(Despesa)