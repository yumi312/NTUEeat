# Generated by Django 4.0.6 on 2022-08-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eatforum', '0006_eatforum_image_alter_eatforum_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eatforum',
            name='category',
        ),
        migrations.AddField(
            model_name='eatforum',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categoryforum', to='eatforum.categoryforum'),
        ),
    ]