# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Track.flac'
        db.delete_column('pages_track', 'flac')


    def backwards(self, orm):
        # Adding field 'Track.flac'
        db.add_column('pages_track', 'flac',
                      self.gf('django.db.models.fields.files.FileField')(default='hello', max_length=100, blank=True),
                      keep_default=False)


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ogg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'wav': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']