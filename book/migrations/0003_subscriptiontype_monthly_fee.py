# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_subscription_extra_shipments'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptiontype',
            name='monthly_fee',
            field=models.FloatField(default=0),
        ),
    ]
