# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x_position', models.FloatField()),
                ('y_position', models.FloatField()),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Entity')),
            ],
        ),
    ]