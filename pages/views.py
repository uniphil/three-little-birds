from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from pages.models import Feature, Poster, Track, Biography
from functools import wraps


def selectable(func):
    nav_links = (
        ('Bio', 'bio'),
        ('Gallery', 'gallery'),
        ('Media', 'media'),
        ('Store', 'store'),
        ('Contact', 'contact'),
    )
    nav = [(n, l, True if l == func.__name__ else False) for n, l in nav_links]
    print nav

    @wraps(func)
    def with_nav(*args, **kwargs):
        return func(nav, *args, **kwargs)

    return with_nav


@selectable
def home(nav, request):
    print nav
    feature = Feature.objects.get(featured=True).inflate()
    track = Track.objects.get(featured=True).inflate()
    poster = Poster.objects.get(featured=True)
    context = RequestContext(request, {
        'nav': nav,
        'feature': feature,
        'track': track,
        'poster': poster,
    })
    return render_to_response('home.html', context)


@selectable
def bio(nav, request):
    print nav
    bio = Biography.objects.get()
    context = RequestContext(request, {
        'nav': nav,
        'bio': bio
    })
    return render_to_response('bio.html', context)


@selectable
def gallery(nav, request):
    return HttpResponse('blah')


@selectable
def media(nav, request):
    return HttpResponse('blah')


@selectable
def store(nav, request):
    return HttpResponse('blah')


@selectable
def contact(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('contact.html', context)


## stupid stuff


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
