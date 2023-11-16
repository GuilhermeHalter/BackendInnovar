from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router

from Innovar.views import PacoteViewSet, ProcedimentoViewSet, HorariosBloqueadoViewSet

router = DefaultRouter()
router.register(r"pacotes", PacoteViewSet)
router.register(r"procedimentos", ProcedimentoViewSet)
router.register(r"horario_bloqueado", HorariosBloqueadoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)