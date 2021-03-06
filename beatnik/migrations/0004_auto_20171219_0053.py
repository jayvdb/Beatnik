# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatnik', '0003_auto_20171113_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_type', models.CharField(choices=[('A', 'Album'), ('T', 'Track')], max_length=1, verbose_name='Album or Track')),
                ('name', models.CharField(max_length=200, verbose_name='Track Name')),
                ('artist', models.CharField(max_length=200, verbose_name='Artist Name')),
                ('album', models.CharField(blank=True, max_length=200, verbose_name='Album Name')),
                ('apple_url', models.URLField(verbose_name='Apple Music URL')),
                ('gpm_url', models.URLField(verbose_name='Google Play Music URL')),
                ('soundcloud_url', models.URLField(verbose_name='Soundcloud URL')),
                ('spotify_url', models.URLField(verbose_name='Spotify URL')),
                ('match_rating', models.IntegerField(default=0, verbose_name='Rating of the match')),
                ('insertion_date', models.DateTimeField(verbose_name='Date of initial insertion')),
                ('update_date', models.DateTimeField(verbose_name='Date of last update')),
                ('artwork', models.URLField(verbose_name='Album art URL')),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
