from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from mainapp.views import UserViewSet, UrlViewSet, redirect_to

router = routers.SimpleRouter()

router.register('api/v1/registration', UserViewSet, basename='user')
router.register('api/v1/short', UrlViewSet, basename='short')

urlpatterns = [
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<url>/', redirect_to, name='redirect'),
]
urlpatterns += router.urls
