# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-24 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rca', '0062_programmepage_ma_entry_requirements_link_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmepage',
            old_name='programme_specification',
            new_name='programme_specification_document',
        ),
    ]