from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('profile', views.UserViewSet)


urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),
]
