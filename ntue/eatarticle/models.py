import re
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


class Hashtag(models.Model):
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(editable=False, blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Hashtag, self).save()


class Eatarticle(models.Model):
    title = models.CharField(max_length=255, default="")
    author_name = models.ForeignKey(User,  on_delete=models.CASCADE)
    snippet = models.CharField(
        max_length=100, default="Click Link Above To Read Blog Post...")
    contents = RichTextField(blank=True, null=True)
    slug = models.SlugField(editable=False, blank=True, default="")
    hashtag = models.ForeignKey(
        Hashtag, null=True, on_delete=models.PROTECT)  # 分哪裡美食等等的分類
    image = models.ImageField(default="", blank=True, upload_to="images")
    list_image = ImageSpecField(source='image', processors=[ResizeToFill(
        350, 200)], format='JPEG', options={'quality': 60})
    detail_image = ImageSpecField(source='image', processors=[
                                  ResizeToFill(700, 400)], format='JPEG', options={'quality': 60})
    edit_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now=True)
    """ likes = models.ManyToManyField(User, related_name='blog_posts')

    def number_of_likes(self):
        return self.likes.count() """

    def __str__(self):
        return '%s - %s' % (self.title, self.author_name)

    class Meta:
        ordering = ['id']
        db_table = "eatarticle"

    def save(self, *args, **kwargs):
        self.slug = uuslug_slugify(self.title)
        super(Eatarticle, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])


class Comment(models.Model):
    eatarticle = models.ForeignKey(
        Eatarticle, editable=False, related_name="comments", on_delete=models.CASCADE)
    author_name = models.ForeignKey(
        User, editable=False, null=True, on_delete=models.PROTECT)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.eatarticle.title, self.author_name)
