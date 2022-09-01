# Generated by Django 4.0.6 on 2022-08-25 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eatforum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatforum',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eatforum',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eatforum',
            name='hashtag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hashtagforum', to='eatforum.hashtagforum'),
        ),
    ]
