# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-11 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('rca', '0086_schoolpageresearchlinks_allow_to_add_external_links'),
        ('taxonomy', '0019_auto_20160901_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardStreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, help_text=b'', max_length=255)),
                ('collapse_upcoming_events', models.BooleanField(default=False, help_text=b'')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('strapline', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'overlay_text', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False))])), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quotation', wagtail.wagtailcore.blocks.CharBlock(classname=b'title')), (b'quotee', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'quotee_job_title', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'full', b'Full-width'), (b'right', b'Right')], default=b'full'))])), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'callout', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), (b'text', wagtail.wagtailcore.blocks.TextBlock()), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'overlay_text', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False))])), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(label=b'External link', required=False)), (b'link_page', wagtail.wagtailcore.blocks.URLBlock(required=False))]), template=b'standard_stream_page/blocks/carousel_block.html'))])),
                ('twitter_feed', models.CharField(blank=True, help_text=b'Replace the default Twitter feed by providing an alternative Twitter handle (without the @ symbol)', max_length=255)),
                ('show_on_homepage', models.BooleanField(default=False)),
                ('show_on_school_page', models.BooleanField(default=False)),
                ('feed_image', models.ForeignKey(blank=True, help_text=b'The image displayed in content feeds, such as the news carousel. Should be 16:9 ratio.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rca.RcaImage')),
                ('related_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.Area')),
                ('related_programme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.Programme')),
                ('related_school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.School')),
                ('social_image', models.ForeignKey(blank=True, help_text=b'', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rca.RcaImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='StandardStreamPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, help_text=b'', verbose_name=b'External link')),
                ('link_text', models.CharField(blank=True, help_text=b'Link title (or leave blank to use page title)', max_length=255)),
                ('link', models.ForeignKey(blank=True, help_text=b'', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='standard_stream_page.StandardStreamPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardStreamPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='standard_stream_page.StandardStreamPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_stream_page_standardstreampagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='standardstreampage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='standard_stream_page.StandardStreamPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
