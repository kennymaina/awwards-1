# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscars', '0003_auto_20190318_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
