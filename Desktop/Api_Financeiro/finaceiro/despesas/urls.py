#------------------------------------------
#------Criação de URL's do APP Despesas----
#------------------------------------------

from rest_framework import routers
from .views import DespesaViewSet

router = routers.DefaultRouter()
router.register(r'despesas', DespesaViewSet)

urlpatterns = router.urls