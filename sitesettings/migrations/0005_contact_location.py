# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0004_auto_20190111_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.URLField(null=True, verbose_name='URL путь'),
        ),
    ]