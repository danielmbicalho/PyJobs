# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freela', '0007_freela_publico'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='data_inscrito',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]