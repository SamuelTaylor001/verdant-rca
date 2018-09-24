# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0021_auto_20170629_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]
