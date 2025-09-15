from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("common.urls")),
    path("api/", include("users.urls")),
    path("api/", include("recipes.urls")),
    path("api/", include("category.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    # JWT Auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Downloadable Schema (YML)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Docs
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls")),
    ]
