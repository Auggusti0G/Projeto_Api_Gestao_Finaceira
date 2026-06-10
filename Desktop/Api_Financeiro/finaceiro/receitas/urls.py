#----------------------------------------------
#-------Craiação do URL's do App de receitas---
#----------------------------------------------

from rest_framework import routers
from .views import ReceitaViewSet

router = routers.DefaultRouter()
router.register(r'receitas', ReceitaViewSet)

urlpatterns = router.urls