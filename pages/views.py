from functools import wraps
# from markdown import markdown
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators import cache_page
from pages.models import Feature, Poster, Track, Biography, GalleryPhoto, Press
from pages.forms import ContactForm, NewsletterForm, FormError


CACHE_PAGE_TIME = 60 * 60


NAV = (
    ('Bio', 'bio'),
    ('Gallery', 'gallery'),
    ('Media', 'media'),
    ('Store', 'store'),
    ('Contact', 'contact'),
)


def selectable(select):
    nav_select = lambda s: [(n, l, True if l == s else False) for n, l in NAV]

    def wrap_with_nav(nav, func):
        @wraps(func)
        def with_nav(*args, **kwargs):
            return func(nav, *args, **kwargs)
        return with_nav

    if isinstance(select, str):
        nav = nav_select(select)
        return lambda func: wrap_with_nav(nav, func)
    else:
        nav = nav_select(select.__name__)
        return wrap_with_nav(nav, select)


@cache_page(CACHE_PAGE_TIME)
@selectable
def home(nav, request):
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

@cache_page(CACHE_PAGE_TIME)
@selectable
def bio(nav, request):
    bio = Biography.objects.get()
    context = RequestContext(request, {
        'nav': nav,
        'bio': bio,
    })
    return render_to_response('bio.html', context)

@cache_page(CACHE_PAGE_TIME)
@selectable
def gallery(nav, request):
    gallery = GalleryPhoto.objects.all().order_by('weight')
    context = RequestContext(request, {
        'gallery': gallery,
        'nav': nav,
    })
    return render_to_response('gallery.html', context)

@cache_page(CACHE_PAGE_TIME)
@selectable(select='gallery')
def galleryphoto(nav, request, photo_id):
    photo = get_object_or_404(GalleryPhoto, pk=photo_id)
    context = RequestContext(request, {
        'photo': photo,
        'nav': nav,
    })
    return render_to_response('gallery_photo.html', context)

@cache_page(CACHE_PAGE_TIME)
@selectable
def media(nav, request):
    press = Press.objects.all()
    bad = press.filter(bad_press=True)
    good = press.exclude(bad_press=True).filter(image="")
    good_featured = press.exclude(bad_press=True).exclude(image="")
    context = RequestContext(request, {
        'good_featured': good_featured,
        'good': good,
        'bad': bad,
        'nav': nav,
    })
    return render_to_response('media.html', context)

@cache_page(CACHE_PAGE_TIME)
@selectable
def store(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('store.html', context)

@cache_page(CACHE_PAGE_TIME)
@selectable
def contact(nav, request):
    if request.method == 'POST':
        try:
            if request.POST.get('form') == 'contact':
                form = ContactForm(request.POST)
                form.send()
                return HttpResponseRedirect('/message-sent')
            elif request.POST.get('form') == 'newsletter':
                form = NewsletterForm(request.POST)
                form.subscribe()
                return HttpResponseRedirect('/subscribed')
            else:
                form = ContactForm()
        except FormError:
           form = ContactForm()
    else:
        form = ContactForm()  # actually arbitrary?

    context = RequestContext(request, {
        'nav': nav,
        'form': form,
    })
    return render_to_response('contact.html', context)
@cache_page(CACHE_PAGE_TIME)
@selectable(select='contact')
def sent(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('message_sent.html', context)
@cache_page(CACHE_PAGE_TIME)
@selectable(select='contact')
def subd(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('subscribed.html', context)



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
