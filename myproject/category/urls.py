from rest_framework.routers import DefaultRouter
from .views import categoryviewsets

router = DefaultRouter()

router.register(
    "categories",
    categoryviewsets
)

urlpatterns = router.urls