from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import productviewsets
from .views import RegisterView, LoginView

router = DefaultRouter()

router.register(
    "products",
    productviewsets
)

from django.urls import path, include

urlpatterns = [

    path(
        "register/",
        RegisterView.as_view()
    ),

    path(
        "login/",
        LoginView.as_view()
    ),

    path(
        "",
        include(router.urls)
    ),
]

