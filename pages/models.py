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
