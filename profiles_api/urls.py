from django.urls import path

from profiles_api import views


urlpatterns = [
    path('', views.ProfileList.as_view()),
    path('<int:pk>/', views.ProfileDetail.as_view()),
]