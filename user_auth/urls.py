from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserAuthViewSet, LoginView, LogoutView

router = DefaultRouter()
router.register('users', UserAuthViewSet, basename='user-list')
router.register('login', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('account/logout/', LogoutView.as_view(), name='logout')
]