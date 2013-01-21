from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from pages.models import Feature

def home(request):
    dbfeature = Feature.objects.get(featured=True)
    feature = {
        'title': dbfeature.title,
        'img': {
            'src': dbfeature.photo,
            'alt': dbfeature.photo_alt,
            'title': dbfeature.photo_title,
        },
        'content': dbfeature.content,
    }
    if dbfeature.more_link:
        feature['more'] = {
            'href': dbfeature.more_link,
            'title': dbfeature.more_title,
        }

    context = {'feature': feature}
    return render_to_response('home.html',
        context_instance=RequestContext(request, context))
