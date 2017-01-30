# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20170122_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='albums', to='imager_images.Image'),
        ),
    ]