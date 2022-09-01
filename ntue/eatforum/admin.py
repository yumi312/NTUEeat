from django.contrib import admin
from .models import  Hashtagforum, Eatforum, Commentforum,Categoryforum

admin.site.register(Categoryforum)
admin.site.register(Hashtagforum)
admin.site.register(Eatforum)
admin.site.register(Commentforum)
# Register your models here.
