# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_post',
            name='file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='topic_post',
            name='file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]