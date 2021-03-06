# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20171017_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='facebook_url',
            field=models.CharField(blank=True, default='https://www.facebook.com/your_username', max_length=100, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='github_url',
            field=models.CharField(blank=True, default='https://www.github.com/your_username', max_length=100, null=True, verbose_name='Github URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='instagram_url',
            field=models.CharField(blank=True, default='https://www.instagram.com/your_username', max_length=100, null=True, verbose_name='Instagram URL'),
        ),
        migrations.AlterField(
            model_name='member',
            name='twitter_url',
            field=models.CharField(blank=True, default='https://www.twitter.com/your_username', max_length=100, null=True, verbose_name='Twitter URL'),
        ),
    ]
