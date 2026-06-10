#----------------------------------
#----Resgistro do app de Receita---
#----------------------------------


from django.contrib import admin
from .models import Receita

admin.site.register(Receita)