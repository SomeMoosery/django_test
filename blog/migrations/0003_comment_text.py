# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
