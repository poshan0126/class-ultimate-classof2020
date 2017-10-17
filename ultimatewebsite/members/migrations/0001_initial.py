# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('image', models.ImageField(upload_to='members')),
                ('phone_number', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Phone Number')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('hometown', models.CharField(max_length=200, verbose_name='Your HomeTown')),
                ('favourite_quote', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField()),
                ('your_website', models.URLField()),
                ('facebook_url', models.CharField(blank=True, max_length=100, verbose_name='Facebook URL')),
                ('twitter_url', models.CharField(blank=True, max_length=100, verbose_name='Twitter URL')),
                ('instagram_url', models.CharField(blank=True, max_length=100, verbose_name='Instagram URL')),
                ('github_url', models.CharField(blank=True, max_length=100, verbose_name='Github URL')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]