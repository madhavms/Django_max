# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
    ]