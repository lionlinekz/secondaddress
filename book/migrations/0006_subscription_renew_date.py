# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-11 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20160410_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='renew_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 11, 9, 0, 303734)),
        ),
    ]