from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'dob', 'bio',]
        help_texts = {k:"" for k in fields}
        #     "username": None,
        #     "Password1": None,
        # }
        widgets = {

        'dob':forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder':'Select a date',
                    'type':'date',
                    }
            ),

        'bio':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Tell me about yourself',

                }
            )
        }



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'dob', 'bio',]
        help_texts = {k:"" for k in fields}
    
        widgets = {

        'dob':forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder':'Select a date',
                    'type':'date',
                    }
            ),

        'bio':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Tell me about yourself',

                }
            )
        }

