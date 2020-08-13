from django.urls import path
from .views import CreateAccountView, UserProfile, ProfileUpdateView
from . import views 

app_name = "users"

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='CreateAccount'),
    path('user-profile/', UserProfile.as_view(), name='UserProfile'),
    path('update-profile/<int:pk>/', ProfileUpdateView.as_view(), name='updateProfile'),
]