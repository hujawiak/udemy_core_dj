# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='My description', null=True),
        ),
    ]
