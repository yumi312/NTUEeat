from django import forms
from .models import Comment
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Comment

        fields = "__all__"

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
        }
        labels = {
            'body': '',
            
        }
