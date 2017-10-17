# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
"""
    dependencies = [
        ('members', '0001_initial'),
    ]
  """

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=10, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='member',
            name='your_website',
            field=models.URLField(blank=True, default='https://pythonair.me', null=True),
        ),
    ]
