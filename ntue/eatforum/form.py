from unicodedata import category
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Eatforum
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Eatforum

        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            #'author_name': forms.Select(attrs={'class': 'form-control  mb-2 input-group'}),
            'contents': forms.Textarea(attrs={'class': 'form-control mb-2 input-group'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            # dropdowm list
            'category': forms.Select(attrs={'class': 'form-control mb-2 input-group'}),
            'hashtag': forms.Select(attrs={'class': 'form-control mb-2 input-group'}),
        }
        labels = {
            'title': '標題',
            'image':'封面圖片',
            #'image':'封面圖片',
            #'author_name': '作者',      # labels['title']
            'contents': '內容',
            'category':'看版',
            'hashtag':'hashtag',
        }
