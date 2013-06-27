from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, SmartResize, Adjust

#from south.modelsinspector import add_introspection_rules
#add_introspection_rules([], ["^imagekit\.models\.ImageSpecField"])


# these numbers come from main.less
ONE_COL = 288
TWO_COL = 616
TRE_COL = 944


class Feature(models.Model):
    """Articles on the home page."""

    title = models.CharField(max_length=80)
    featured = models.BooleanField(default=False)
    photo = models.FileField(upload_to='three-little-birds/features/photos',
                             blank=True)
    photo_web = ImageSpecField(source='photo',
                         processors=[ResizeToFit(TWO_COL)],
                         format='JPEG',
                         options={'quality': 87})
    photo_alt = models.CharField(max_length=80, blank=True)
    photo_title = models.CharField(max_length=80, blank=True)
    content = models.TextField()
    more_link = models.SlugField(blank=True)
    more_title = models.CharField(max_length=80, blank=True)

    def inflate(self):
        inflated = {
            'title': self.title,
            'photo': self.photo_web,
            'photo_alt': self.photo_alt,
            'photo_title': self.photo_title,
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


class GalleryPhoto(models.Model):
    """Photos in the gallery"""

    photo = models.FileField(upload_to='three-little-birds/gallery',
                             blank=False)
    web = ImageSpecField(source='photo',
                         processors=[ResizeToFit(TRE_COL)],
                         format='JPEG',
                         options={'quality': 91})
    thumbnail = ImageSpecField(source='photo',
                               processors=[
                                    Adjust(color=0.25),
                                    SmartResize(288, 288),
                               ],
                               format='JPEG',
                               options={'quality': 78})
    caption = models.TextField()
    weight = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        return '{}: {}'.format(self.weight, self.caption[:21])


class Press(models.Model):
    """What they're saying about TLB"""

    publication = models.CharField(max_length=120, blank=False)
    author = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=120, blank=True)
    date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True)
    bad_press = models.BooleanField(default=False, blank=True)
    story = models.TextField(blank=True)
    image = models.ImageField(upload_to='three-little-birds/press-images', blank=True)
    image_thumb = ImageSpecField(source='image',
                                 processors=[
                                    Adjust(color=0.25),
                                    SmartResize(288, 288),
                                 ],
                                 format='JPEG',
                                 options={'quality': 81})

    def __unicode__(self):
        return '{} {}: {}'.format(self.date, self.publication, self.title)
