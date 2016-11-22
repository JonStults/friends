# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('alias', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(max_length=45)),
                ('date_of_birth', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
