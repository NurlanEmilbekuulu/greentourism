# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190111_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='tour',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='index.Tour'),
            preserve_default=False,
        ),
    ]
