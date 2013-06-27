# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feature'
        db.create_table('pages_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('photo_alt', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('photo_title', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('more_link', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('more_title', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('pages', ['Feature'])

        # Adding model 'Poster'
        db.create_table('pages_poster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('alt_text', self.gf('django.db.models.fields.TextField')()),
            ('tooltip', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('link_to', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('pages', ['Poster'])

        # Adding model 'Track'
        db.create_table('pages_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mp3', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('ogg', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('flac', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('wav', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pages', ['Track'])

        # Adding model 'Biography'
        db.create_table('pages_biography', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Biography', max_length=80)),
            ('content1', self.gf('django.db.models.fields.TextField')()),
            ('ad', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('content2', self.gf('django.db.models.fields.TextField')()),
            ('instrumentation', self.gf('django.db.models.fields.TextField')()),
            ('discography', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pages', ['Biography'])

        # Adding model 'GalleryPhoto'
        db.create_table('pages_galleryphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('pages', ['GalleryPhoto'])

        # Adding model 'Press'
        db.create_table('pages_press', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('bad_press', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('story', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pages', ['Press'])


    def backwards(self, orm):
        # Deleting model 'Feature'
        db.delete_table('pages_feature')

        # Deleting model 'Poster'
        db.delete_table('pages_poster')

        # Deleting model 'Track'
        db.delete_table('pages_track')

        # Deleting model 'Biography'
        db.delete_table('pages_biography')

        # Deleting model 'GalleryPhoto'
        db.delete_table('pages_galleryphoto')

        # Deleting model 'Press'
        db.delete_table('pages_press')


    models = {
        'pages.biography': {
            'Meta': {'object_name': 'Biography'},
            'ad': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'content1': ('django.db.models.fields.TextField', [], {}),
            'content2': ('django.db.models.fields.TextField', [], {}),
            'discography': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrumentation': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Biography'", 'max_length': '80'})
        },
        'pages.feature': {
            'Meta': {'object_name': 'Feature'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'more_link': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'more_title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_alt': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'photo_title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'pages.galleryphoto': {
            'Meta': {'object_name': 'GalleryPhoto'},
            'caption': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'pages.poster': {
            'Meta': {'object_name': 'Poster'},
            'alt_text': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_to': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        'pages.press': {
            'Meta': {'object_name': 'Press'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'bad_press': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'publication': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'story': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        },
        'pages.track': {
            'Meta': {'object_name': 'Track'},
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flac': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ogg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'wav': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']