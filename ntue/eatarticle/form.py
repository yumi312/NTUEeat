from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Eatarticle
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Eatarticle

        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            'author_name': forms.Select(attrs={'class': 'form-control  mb-2 input-group'}),
            'contents': forms.Textarea(attrs={'class': 'form-control mb-2 input-group'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            # dropdowm list
            'hashtag': forms.Select(attrs={'class': 'form-control mb-2 input-group'}),
        }
        labels = {
            'title': '名稱',
            'author_name': '作者',      # labels['title']
            'contents': '內容',
            'slug': '代號',
            'hashtag':'Hashtag',
        }
