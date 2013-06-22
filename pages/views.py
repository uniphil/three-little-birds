from functools import wraps
# from markdown import markdown
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from pages.models import Feature, Poster, Track, Biography, GalleryPhoto
from pages.forms import ContactForm


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


@selectable
def bio(nav, request):
    bio = Biography.objects.get()
    context = RequestContext(request, {
        'nav': nav,
        'bio': bio,
    })
    return render_to_response('bio.html', context)


@selectable
def gallery(nav, request):
    gallery = GalleryPhoto.objects.all()
    context = RequestContext(request, {
        'gallery': gallery,
        'nav': nav,
    })
    return render_to_response('gallery.html', context)


@selectable(select='gallery')
def galleryphoto(nav, request, photo_id):
    photo = get_object_or_404(GalleryPhoto, pk=photo_id)
    context = RequestContext(request, {
        'photo': photo,
        'nav': nav,
    })
    return render_to_response('gallery_photo.html', context)


@selectable
def media(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('media.html', context)


@selectable
def store(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('store.html', context)


@selectable
def contact(nav, request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email'],
            data = {
                'to': ['uniphil@gmail.com'],
                'from': sender,
                'subject': '[TLB Contact Form] message from {}'.format(name),
                'text': form.cleaned_data['message']
            }
            if form.cleaned_data['cc']:
                data['cc'] = sender

            # SEND THAT SHIT
            import os, requests
            mailgun_response = requests.post(
                "https://api.mailgun.net/v2/threelittlebirds.herouapp.com/messages",
                auth=('api', os.environ.get('MAILGUN_API_KEY')),
                data=data,
            )

            print mailgun_response
            print mailgun_response.text

            return HttpResponseRedirect('/message-sent')
    else:
        form = ContactForm()

    context = RequestContext(request, {
        'nav': nav,
        'form': form,
    })
    return render_to_response('contact.html', context)

@selectable(select='contact')
def sent(nav, request):
    context = RequestContext(request, {
        'nav': nav,
    })
    return render_to_response('message_sent.html', context)


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
