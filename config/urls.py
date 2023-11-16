from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from Innovar.views import PacoteViewSet, ProcedimentoViewSet, HorariosBloqueadoViewSet

router = DefaultRouter()
router.register(r"pacotes", PacoteViewSet)
router.register(r"procedimentos", ProcedimentoViewSet)
router.register(r"horario_bloqueado", HorariosBloqueadoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]