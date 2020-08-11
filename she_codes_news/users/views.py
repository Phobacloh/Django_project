from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()

class CreateAccountView(generic.edit.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfile(generic.edit.FormView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'users/UserProfile.html'
# Create your views here.
