# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190111_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rate',
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=1),
        ),
    ]
