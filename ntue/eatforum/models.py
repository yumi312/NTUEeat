import re
from unicodedata import category
from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify as django_slugify
from uuslug import slugify as uuslug_slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

import time
# Create your models here.
class Hashtagforum(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(editable=False,blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Hashtagforum, self).save()

class Categoryforum(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(editable=False,blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Categoryforum, self).save()

class Eatforum(models.Model):
    title = models.CharField(max_length=255, default="")
    author_name = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='author_name')
    snippet = models.CharField(editable=False,max_length=100, default="")
    slug = models.SlugField(editable=False,blank=True, default="")
    contents = RichTextField(blank=True,null=True)
    category = models.ForeignKey(Categoryforum, null=True, on_delete=models.PROTECT,related_name='categoryforum')# 分成 美食、校園、團購等等的分類
    hashtag = models.ForeignKey(Hashtagforum, null=True, on_delete=models.PROTECT,related_name='hashtagforum')  # hashtag
    likes = models.ManyToManyField(User, related_name='like',default=None,blank=True),
    like_count = models.BigIntegerField(default="0"),
    edit_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="", blank=True, upload_to="images")
    list_image = ImageSpecField(source='image',processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})
    """ likes = models.ManyToManyField(User, related_name='blog_posts')"""

    
    def __str__(self):
        return '%s - %s' % (self.title, self.author_name)

    class Meta:
        ordering = ['id']
        db_table = "eatforum"

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Eatforum, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

class Commentforum(models.Model):
    eatforum = models.ForeignKey(Eatforum,editable=False,related_name="comments", on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, editable=False,null=True, on_delete=models.PROTECT)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.eatforum.title, self.author_name)