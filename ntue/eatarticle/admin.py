from django.contrib import admin
from .models import Author, Hashtag, Eatarticle

# Register your models here.
admin.site.register(Author)
admin.site.register(Hashtag)
admin.site.register(Eatarticle)