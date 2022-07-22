from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.utils.text import slugify as django_slugify
from uuslug import slugify as uuslug_slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

import time
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

class Hashtag(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(editable=False,blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Hashtag, self).save()

class Eatarticle(models.Model):
    title = models.CharField(max_length=255, default="")
    author_name = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
    contents = models.TextField(default="")
    slug = models.SlugField(editable=False,blank=True, default="")
    hashtag = models.ForeignKey(Hashtag, null=True, on_delete=models.PROTECT)  # 分成 程式、美術等等的分類
    image = models.ImageField(default="", blank=True, upload_to="images")
    list_image = ImageSpecField(source='image',processors=[ResizeToFill(350, 200)], format='JPEG', options={'quality': 60})
    detail_image = ImageSpecField(source='image',processors=[ResizeToFill(700, 400)], format='JPEG', options={'quality': 60})
    edit_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now=True)
    #上面兩個不知道有甚麼區別
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        db_table = "eatarticle"

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Eatarticle, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])