# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0007_object_pk_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='actor_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='actor name'),
        ),
    ]
