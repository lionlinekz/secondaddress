# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20160411_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='renew_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 11, 14, 32, 50, 588026)),
        ),
    ]
