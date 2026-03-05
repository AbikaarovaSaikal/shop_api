from django.urls import path
from .views import (
    RegistrationAPIView,
    AuthorizationAPIView,
    ConfirmUserAPIView,
    CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', AuthorizationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/jwt/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]