from django.urls import path
from .views import CreateAccountView, UserProfile
from . import views 

app_name = "users"

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='CreateAccount'),
    path('user-profile/', UserProfile.as_view(), name='UserProfile'),
]