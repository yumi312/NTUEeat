# Generated by Django 4.0.6 on 2022-08-26 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eatforum', '0005_alter_eatforum_author_name_alter_eatforum_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatforum',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='eatforum',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
