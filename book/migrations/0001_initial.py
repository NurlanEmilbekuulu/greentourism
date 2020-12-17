# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 18:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('rooms', models.PositiveIntegerField()),
                ('adults', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Room')),
            ],
            options={
                'verbose_name': 'Бронирование Комнаты',
                'verbose_name_plural': 'Бронирование Комнат',
            },
        ),
        migrations.CreateModel(
            name='BookingTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('adults', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Tour')),
            ],
            options={
                'verbose_name': 'Бронирование Тура',
                'verbose_name_plural': 'Бронирование Туров',
            },
        ),
    ]