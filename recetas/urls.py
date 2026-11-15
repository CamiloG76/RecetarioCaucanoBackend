from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet

router = DefaultRouter()
router.register(r'recetas', RecetaViewSet)

urlpatterns = router.urls
