# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180909_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='a_cover',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
