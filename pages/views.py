# from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from pages.models import Feature, Track, Poster


def home(request):
    db_feature = Feature.objects.get(featured=True)
    feature = {
        'title': db_feature.title,
        'img': {
            'src': db_feature.photo,
            'alt': db_feature.photo_alt,
            'title': db_feature.photo_title,
        },
        'content': db_feature.content,
    }
    if db_feature.more_link:
        feature['more'] = {
            'href': db_feature.more_link,
            'title': db_feature.more_title,
        }

    db_track = Track.objects.get(featured=True)
    track = {
        'name': db_track.name,
        'formats': []
    }
    if db_track.mp3:
        track['formats'].append({
            'name': 'mp3',
            'url': db_track.mp3
        })
    if db_track.ogg:
        track['formats'].append({
            'name': 'ogg vorbis',
            'url': db_track.ogg
        })
    if db_track.flac:
        track['formats'].append({
            'name': 'lossless flacc',
            'url': db_track.flac
        })
    if db_track.wav:
        track['formats'].append({
            'name': 'uncompressed wav',
            'url': db_track.wav
        })

    db_poster = Poster.objects.get(featured=True)

    context = {
        'feature': feature,
        'track': track,
        'poster': db_poster,
    }
    return render_to_response('home.html',
        context_instance=RequestContext(request, context))
