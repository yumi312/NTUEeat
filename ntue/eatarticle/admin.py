from django.contrib import admin
from .models import  Hashtag, Eatarticle, Comment

# Register your models here.

admin.site.register(Hashtag)
admin.site.register(Eatarticle)
admin.site.register(Comment)