# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_about_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='application',
            field=models.CharField(default='d', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='datafilter',
            field=models.CharField(default='d', max_length=100),
            preserve_default=False,
        ),
    ]