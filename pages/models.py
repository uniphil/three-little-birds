from django.db import models


class Feature(models.Model):
    """Articles on the home page."""

    title = models.CharField(max_length=80)
    featured = models.BooleanField(default=False)
    photo = models.FileField(upload_to='three-little-birds/features/photos', blank=True)
    photo_alt = models.CharField(max_length=80, blank=True)
    photo_title = models.CharField(max_length=80, blank=True)
    content = models.TextField()
    more_link = models.SlugField(blank=True)
    more_title = models.CharField(max_length=80, blank=True)

    def inflate(self):
        inflated = {
            'title': self.title,
            'img': {
                'src': self.photo,
                'alt': self.photo_alt,
                'title': self.photo_title,
            },
            'content': self.content,
        }
        if self.more_link:
            inflated['more'] = {
                'href': self.more_link,
                'title': self.more_title,
            }
        return inflated

    def __unicode__(self):
        return self.title


class Poster(models.Model):
    """Large photo on the home page."""

    featured = models.BooleanField(default=False)
    photo = models.FileField(upload_to='three-little-birds/posters', blank=False)
    alt_text = models.TextField()
    tooltip = models.CharField(max_length=180, blank=False)
    link_to = models.URLField(blank=True)

    def __unicode__(self):
        return self.tooltip


class Track(models.Model):
    """Music!"""

    name = models.CharField(max_length=120)
    featured = models.BooleanField(default=False)
    mp3 = models.FileField(upload_to='three-little-birds/tracks/mp3', blank=True)
    ogg = models.FileField(upload_to='three-little-birds/tracks/ogg', blank=True)
    flac = models.FileField(upload_to='three-little-birds/tracks/flac', blank=True)
    wav = models.FileField(upload_to='three-little-birds/tracks/wav', blank=True)

    def inflate(self):
        inflated = {
            'name': self.name,
            'formats': []
        }
        if self.mp3:
            inflated['formats'].append({
                'name': 'mp3',
                'url': self.mp3
            })
        if self.ogg:
            inflated['formats'].append({
                'name': 'ogg vorbis',
                'url': self.ogg
            })
        if self.flac:
            inflated['formats'].append({
                'name': 'lossless flacc',
                'url': self.flac
            })
        if self.wav:
            inflated['formats'].append({
                'name': 'uncompressed wav',
                'url': self.wav
            })
        return inflated

    def __unicode__(self):
        return self.name


class Biography(models.Model):
    """Stuff on the bio page."""

    title = models.CharField(max_length=80, default="Biography")
    content1 = models.TextField()
    ad = models.FileField(upload_to='three-little-birds/bio-ads')
    photo = models.FileField(upload_to='three-little-birds/bio-photos')
    content2 = models.TextField()
    instrumentation = models.TextField()
    discography = models.TextField()

    def __unicode__(self):
        return self.title

