from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'bio')
