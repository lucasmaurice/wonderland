# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170715_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='person_name',
        ),
        migrations.RemoveField(
            model_name='object',
            name='color',
        ),
        migrations.RemoveField(
            model_name='object',
            name='type',
        ),
        migrations.RemoveField(
            model_name='room',
            name='doors',
        ),
        migrations.RemoveField(
            model_name='room',
            name='entity',
        ),
        migrations.AddField(
            model_name='door',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AddField(
            model_name='entity',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AddField(
            model_name='human',
            name='operator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='object',
            name='categorie',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='object',
            name='probabilty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='human',
            name='entity',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Entity'),
        ),
        migrations.AlterField(
            model_name='object',
            name='entity',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Entity'),
        ),
    ]
