from django.urls import path
from .views import CreateAccountView

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='CreateAccount')
]