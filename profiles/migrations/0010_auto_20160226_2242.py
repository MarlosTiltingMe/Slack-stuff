# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160218135022 on 2016-02-26 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20160226_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='id',
        ),
        migrations.AlterField(
            model_name='posts',
            name='title_text',
            field=models.CharField(max_length=72, primary_key=True, serialize=False),
        ),
    ]