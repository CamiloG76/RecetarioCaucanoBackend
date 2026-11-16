
from rest_framework.routers import DefaultRouter
from .views import IngredienteViewSet

router = DefaultRouter()

router.register(
    r'ingredientes',
    IngredienteViewSet,
    basename='ingrediente'
)

urlpatterns = router.urls
