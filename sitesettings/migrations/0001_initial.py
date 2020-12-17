# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.URLField(verbose_name='Название сайта')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('icon', models.CharField(max_length=255, verbose_name='Иконка')),
                ('url', models.URLField(verbose_name='URL путь')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]
