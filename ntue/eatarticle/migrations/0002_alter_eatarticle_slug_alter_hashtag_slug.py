# Generated by Django 4.0.6 on 2022-07-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatarticle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatarticle',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False),
        ),
    ]
