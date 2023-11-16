from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from Innovar.views import PacoteViewSet, ProcedimentoViewSet

router = DefaultRouter()
router.register(r"pacotes", PacoteViewSet)
router.register(r"procedimentos", ProcedimentoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]