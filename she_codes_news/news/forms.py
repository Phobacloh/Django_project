from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content','image_url']
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'label',
                    'placeholder':'Name your masterpiece',
                }
            ),

            'content':forms.Textarea(
                attrs={
                    'class':'label',
                    'placeholder':'Make ART!',
                }
            ),
                    
            'image_url':forms.URLInput(
                attrs={
                    'class':'label',
                    'placeholder':'Image URL',
                }
            ),

            'pub_date':forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder':'Select a date',
                    'type':'date',
                }
            )
        
        }