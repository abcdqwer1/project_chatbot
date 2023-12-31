from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # API 스키마 제공(yaml파일)
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # 테스트할 수 있는 UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # API 문서화를 위한 UI
    path('jwt-token-auth/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('jwt-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt-token-auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]