# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-30 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh_user', '0005_auto_20170630_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMPLOYEE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('Eid', models.CharField(blank=True, max_length=10, null=True)),
                ('department', models.CharField(blank=True, max_length=10, null=True)),
                ('position', models.CharField(blank=True, max_length=10, null=True)),
                ('trainings', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
