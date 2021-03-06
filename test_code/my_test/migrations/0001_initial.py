# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('partyname', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='../static/img')),
                ('partydesc', models.TextField(max_length=500)),
                ('company', models.CharField(max_length=150)),
                ('contacter', models.CharField(max_length=30)),
                ('releasesta', models.IntegerField(default='1')),
                ('manager_id', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
