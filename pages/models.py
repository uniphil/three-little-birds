from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=80)
    featured = models.BooleanField(default=False)
    photo = models.FileField(upload_to='three-little-birds/features/photos', blank=True)
    photo_alt = models.CharField(max_length=80, blank=True)
    photo_title = models.CharField(max_length=80, blank=True)
    content = models.TextField()
    more_link = models.SlugField(blank=True)
    more_title = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=120)
    featured = models.BooleanField(default=False)
    mp3 = models.FileField(upload_to='three-little-birds/tracks/mp3', blank=True)
    ogg = models.FileField(upload_to='three-little-birds/tracks/ogg', blank=True)
    flac = models.FileField(upload_to='three-little-birds/tracks/flac', blank=True)
    wav = models.FileField(upload_to='three-little-birds/tracks/wav', blank=True)

    def __unicode__(self):
        return self.name


class Poster(models.Model):
    featured = models.BooleanField(default=False)
    photo = models.FileField(upload_to='three-little-birds/posters', blank=False)
    alt_text = models.TextField()
    tooltip = models.CharField(max_length=180, blank=False)
    link_to = models.URLField(blank=True)

    def __unicode__(self):
        return self.tooltip
