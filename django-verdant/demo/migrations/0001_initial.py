# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePageCarouselItem'
        db.create_table(u'demo_homepagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='carousel_items', to=orm['demo.DemoHomePage'])),
        ))
        db.send_create_signal(u'demo', ['HomePageCarouselItem'])

        # Adding model 'HomePageRelatedLink'
        db.create_table(u'demo_homepagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.DemoHomePage'])),
        ))
        db.send_create_signal(u'demo', ['HomePageRelatedLink'])

        # Adding model 'DemoHomePage'
        db.create_table(u'demo_demohomepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('body', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['DemoHomePage'])

        # Adding model 'DemoStandardIndexPage'
        db.create_table(u'demo_demostandardindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'demo', ['DemoStandardIndexPage'])

        # Adding model 'StandardPageCarouselItem'
        db.create_table(u'demo_standardpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='carousel_items', to=orm['demo.DemoStandardPage'])),
        ))
        db.send_create_signal(u'demo', ['StandardPageCarouselItem'])

        # Adding model 'StandardPageRelatedLink'
        db.create_table(u'demo_standardpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.DemoStandardPage'])),
        ))
        db.send_create_signal(u'demo', ['StandardPageRelatedLink'])

        # Adding model 'DemoStandardPage'
        db.create_table(u'demo_demostandardpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('core.fields.RichTextField')(blank=True)),
            ('body', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['DemoStandardPage'])

        # Adding model 'BlogIndexPageRelatedLink'
        db.create_table(u'demo_blogindexpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.BlogIndexPage'])),
        ))
        db.send_create_signal(u'demo', ['BlogIndexPageRelatedLink'])

        # Adding model 'BlogIndexPage'
        db.create_table(u'demo_blogindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['BlogIndexPage'])

        # Adding model 'BlogPageCarouselItem'
        db.create_table(u'demo_blogpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='carousel_items', to=orm['demo.BlogPage'])),
        ))
        db.send_create_signal(u'demo', ['BlogPageCarouselItem'])

        # Adding model 'BlogPageRelatedLink'
        db.create_table(u'demo_blogpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.BlogPage'])),
        ))
        db.send_create_signal(u'demo', ['BlogPageRelatedLink'])

        # Adding model 'BlogPage'
        db.create_table(u'demo_blogpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('body', self.gf('core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'demo', ['BlogPage'])

        # Adding model 'PersonPageRelatedLink'
        db.create_table(u'demo_personpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.PersonPage'])),
        ))
        db.send_create_signal(u'demo', ['PersonPageRelatedLink'])

        # Adding model 'PersonPage'
        db.create_table(u'demo_personpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('intro', self.gf('core.fields.RichTextField')(blank=True)),
            ('biography', self.gf('core.fields.RichTextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
        ))
        db.send_create_signal(u'demo', ['PersonPage'])

        # Adding model 'ContactPage'
        db.create_table(u'demo_contactpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('body', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['ContactPage'])

        # Adding model 'EventIndexPageRelatedLink'
        db.create_table(u'demo_eventindexpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.EventIndexPage'])),
        ))
        db.send_create_signal(u'demo', ['EventIndexPageRelatedLink'])

        # Adding model 'EventIndexPage'
        db.create_table(u'demo_eventindexpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('intro', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['EventIndexPage'])

        # Adding model 'EventPageCarouselItem'
        db.create_table(u'demo_eventpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
            ('embed_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='carousel_items', to=orm['demo.EventPage'])),
        ))
        db.send_create_signal(u'demo', ['EventPageCarouselItem'])

        # Adding model 'EventPageRelatedLink'
        db.create_table(u'demo_eventpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='related_links', to=orm['demo.EventPage'])),
        ))
        db.send_create_signal(u'demo', ['EventPageRelatedLink'])

        # Adding model 'EventPageDatesAndTimes'
        db.create_table(u'demo_eventpagedatesandtimes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='dates_and_times', to=orm['demo.EventPage'])),
            ('date_from', self.gf('django.db.models.fields.DateField')()),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('time_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('time_other', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'demo', ['EventPageDatesAndTimes'])

        # Adding model 'EventPageSpeaker'
        db.create_table(u'demo_eventpagespeaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_external', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['core.Page'])),
            ('link_document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantdocs.Document'])),
            ('page', self.gf('cluster.fields.ParentalKey')(related_name='speakers', to=orm['demo.EventPage'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['verdantimages.Image'])),
        ))
        db.send_create_signal(u'demo', ['EventPageSpeaker'])

        # Adding model 'EventPage'
        db.create_table(u'demo_eventpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('audience', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('core.fields.RichTextField')(blank=True)),
            ('specific_directions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('specific_directions_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('cost', self.gf('core.fields.RichTextField')(blank=True)),
            ('signup_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'demo', ['EventPage'])


    def backwards(self, orm):
        # Deleting model 'HomePageCarouselItem'
        db.delete_table(u'demo_homepagecarouselitem')

        # Deleting model 'HomePageRelatedLink'
        db.delete_table(u'demo_homepagerelatedlink')

        # Deleting model 'DemoHomePage'
        db.delete_table(u'demo_demohomepage')

        # Deleting model 'DemoStandardIndexPage'
        db.delete_table(u'demo_demostandardindexpage')

        # Deleting model 'StandardPageCarouselItem'
        db.delete_table(u'demo_standardpagecarouselitem')

        # Deleting model 'StandardPageRelatedLink'
        db.delete_table(u'demo_standardpagerelatedlink')

        # Deleting model 'DemoStandardPage'
        db.delete_table(u'demo_demostandardpage')

        # Deleting model 'BlogIndexPageRelatedLink'
        db.delete_table(u'demo_blogindexpagerelatedlink')

        # Deleting model 'BlogIndexPage'
        db.delete_table(u'demo_blogindexpage')

        # Deleting model 'BlogPageCarouselItem'
        db.delete_table(u'demo_blogpagecarouselitem')

        # Deleting model 'BlogPageRelatedLink'
        db.delete_table(u'demo_blogpagerelatedlink')

        # Deleting model 'BlogPage'
        db.delete_table(u'demo_blogpage')

        # Deleting model 'PersonPageRelatedLink'
        db.delete_table(u'demo_personpagerelatedlink')

        # Deleting model 'PersonPage'
        db.delete_table(u'demo_personpage')

        # Deleting model 'ContactPage'
        db.delete_table(u'demo_contactpage')

        # Deleting model 'EventIndexPageRelatedLink'
        db.delete_table(u'demo_eventindexpagerelatedlink')

        # Deleting model 'EventIndexPage'
        db.delete_table(u'demo_eventindexpage')

        # Deleting model 'EventPageCarouselItem'
        db.delete_table(u'demo_eventpagecarouselitem')

        # Deleting model 'EventPageRelatedLink'
        db.delete_table(u'demo_eventpagerelatedlink')

        # Deleting model 'EventPageDatesAndTimes'
        db.delete_table(u'demo_eventpagedatesandtimes')

        # Deleting model 'EventPageSpeaker'
        db.delete_table(u'demo_eventpagespeaker')

        # Deleting model 'EventPage'
        db.delete_table(u'demo_eventpage')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'has_unpublished_changes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_pages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'search_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'demo.blogindexpage': {
            'Meta': {'object_name': 'BlogIndexPage', '_ormbases': [u'core.Page']},
            'intro': ('core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.blogindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.BlogIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.blogpage': {
            'Meta': {'object_name': 'BlogPage', '_ormbases': [u'core.Page']},
            'body': ('core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.blogpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.blogpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.contactpage': {
            'Meta': {'object_name': 'ContactPage', '_ormbases': [u'core.Page']},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'body': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'demo.demohomepage': {
            'Meta': {'object_name': 'DemoHomePage', '_ormbases': [u'core.Page']},
            'body': ('core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.demostandardindexpage': {
            'Meta': {'object_name': 'DemoStandardIndexPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.demostandardpage': {
            'Meta': {'object_name': 'DemoStandardPage', '_ormbases': [u'core.Page']},
            'body': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'intro': ('core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.eventindexpage': {
            'Meta': {'object_name': 'EventIndexPage', '_ormbases': [u'core.Page']},
            'intro': ('core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.eventindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.EventIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.eventpage': {
            'Meta': {'object_name': 'EventPage', '_ormbases': [u'core.Page']},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'cost': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'signup_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'specific_directions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'specific_directions_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'demo.eventpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.eventpagedatesandtimes': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageDatesAndTimes'},
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'dates_and_times'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'time_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.eventpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.eventpagespeaker': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageSpeaker'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'speakers'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.homepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.DemoHomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.homepagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.DemoHomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.personpage': {
            'Meta': {'object_name': 'PersonPage', '_ormbases': [u'core.Page']},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'biography': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'intro': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'demo.personpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'PersonPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.PersonPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.standardpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['verdantimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.DemoStandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.standardpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['core.Page']"}),
            'page': ('cluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.DemoStandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.rcaimage': {
            'Meta': {'object_name': 'RcaImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'eprint_docid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'verdantdocs.document': {
            'Meta': {'object_name': 'Document'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'verdantimages.image': {
            'Meta': {'object_name': 'Image'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['demo']