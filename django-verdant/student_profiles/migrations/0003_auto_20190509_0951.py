# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-05-09 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_profiles', '0002_auto_20151208_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofilessettings',
            name='new_student_page_index',
            field=models.ForeignKey(help_text=b'New student pages will be added as children of this page.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page', verbose_name=b'Student pages'),
        ),
        migrations.AlterField(
            model_name='studentprofilessettings',
            name='rca_now_index',
            field=models.ForeignKey(help_text=b'New RCA Now pages will be added as children of this page.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page', verbose_name=b'RCA Now pages'),
        ),
    ]
