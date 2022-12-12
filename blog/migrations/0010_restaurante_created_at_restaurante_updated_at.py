# Generated by Django 4.1.2 on 2022-12-08 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_monumento_image_monumento_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]