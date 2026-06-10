#-----------------------------------------------
#-----Criacao de registro de app de categorias--
#-----------------------------------------------

from django.contrib import admin
from .models import Categoria

admin.site.register(Categoria)