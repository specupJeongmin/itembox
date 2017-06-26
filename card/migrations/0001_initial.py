# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('depth', models.IntegerField(max_length=10)),
                ('level', models.IntegerField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
