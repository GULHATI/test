# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-30 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0004_auto_20170630_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='Eid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='department',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='position',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='Eid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='department',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='position',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
