# Generated by Django 4.0.6 on 2022-08-26 20:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eatforum', '0007_remove_eatforum_category_eatforum_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatforum',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
