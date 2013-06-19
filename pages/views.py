from django.http import HttpResponse
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


def sm2(request):
    import os
    swf_path = os.path.join('pages', 'static', 'swf', 'soundmanager2.swf')
    swf = open(swf_path)
    return HttpResponse(swf, content_type='application/x-shockwave-flash')


def crossdomain(request):
    policy = """<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
    <!-- Read this: www.adobe.com/devnet/articles/crossdomain_policy_file_spec.html -->

    <!-- Most restrictive policy: -->
    <site-control permitted-cross-domain-policies="none"/>

    <!-- Least restrictive policy: -->
    <!--
    <site-control permitted-cross-domain-policies="all"/>
    <allow-access-from domain="*" to-ports="*" secure="false"/>
    <allow-http-request-headers-from domain="*" headers="*" secure="false"/>
    -->
</cross-domain-policy>
"""
    return HttpResponse(policy, content_type='application/xml')
