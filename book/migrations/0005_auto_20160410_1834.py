# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='first_addressee_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='subscription',
            name='first_addressee_phone',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='subscription',
            name='saver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscription',
            name='second_addressee_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='subscription',
            name='second_addressee_phone',
            field=models.CharField(default='', max_length=64),
        ),
    ]
