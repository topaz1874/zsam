# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 07:56
from __future__ import unicode_literals

import devblog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0002_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.FileField(blank=True, upload_to=devblog.models.upload_here),
        ),
    ]