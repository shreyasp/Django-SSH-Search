# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssh_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='password',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
