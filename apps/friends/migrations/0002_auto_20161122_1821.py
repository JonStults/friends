# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
