# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 13:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20160903_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_photo_taken',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 13, 17, 59, 287222, tzinfo=utc), verbose_name='year photo taken'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 13, 17, 59, 288406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(default='146794', max_length=50, verbose_name='name'),
        ),
    ]