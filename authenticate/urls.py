from django.urls import path
from . import views


urlpatterns = [
    # authenticate
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='get-token'),
    path('register/', views.registration_views, name='register'),
    # profiles
    path('profiles/', views.ProfileList.as_view() , name='profile-list'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),


]