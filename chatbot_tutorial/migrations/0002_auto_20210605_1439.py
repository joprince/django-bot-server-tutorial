# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-06-05 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='dumb',
            new_name='dumb_count',
        ),
    ]
