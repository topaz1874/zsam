# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('devblog', '0004_weights'),
    ]

    operations = [
        migrations.AddField(
            model_name='weights',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]