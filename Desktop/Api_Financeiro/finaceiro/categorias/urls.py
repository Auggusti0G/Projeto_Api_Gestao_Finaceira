#-----------------------------------------
#---Craiação de URL's do app Categorias---
#-----------------------------------------


from rest_framework import routers
from .views import CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = router.urls