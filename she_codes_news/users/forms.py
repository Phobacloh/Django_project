from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'dob', 'bio', 'profile_picture']
        widgets = {

        'dob':forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder':'Select a date',
                    'type':'date',
                    }
            )
        
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = ['username', 'email']
        fields = '__all__'

