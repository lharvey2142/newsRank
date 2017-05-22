# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_auto_20170515_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='negative',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='neutral',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='positive',
            field=models.FloatField(blank=True, null=True),
        ),
    ]