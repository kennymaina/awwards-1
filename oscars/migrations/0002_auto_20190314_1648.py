# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
