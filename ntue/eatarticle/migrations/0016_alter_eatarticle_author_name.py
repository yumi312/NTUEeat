# Generated by Django 4.0.6 on 2022-07-29 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eatarticle', '0015_alter_eatarticle_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatarticle',
            name='author_name',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
