# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-30 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('rca', '0086_schoolpageresearchlinks_allow_to_add_external_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, help_text=b'', max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('twitter_feed', models.CharField(blank=True, help_text=b'Replace the default Twitter feed by providing an alternative Twitter handle (without the @ symbol)', max_length=255)),
                ('feed_image', models.ForeignKey(blank=True, help_text=b'The image displayed in content feeds, such as the news carousel. Should be 16:9 ratio.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rca.RcaImage')),
                ('social_image', models.ForeignKey(blank=True, help_text=b'', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rca.RcaImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]