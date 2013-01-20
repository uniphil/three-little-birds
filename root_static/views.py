from django.http import HttpResponse, Http404
import os
root_path = lambda *p: os.path.abspath(os.path.join(__file__, '../static', *p))

def txt(request):
    absolute = root_path(request.path[1:]) # remove preceeding '/'
    try:
        content = open(absolute).read()
    except IOError:
        raise Http404
    return HttpResponse(content, content_type='text/plain')

def png(request):
    absolute = root_path(request.path[1:]) # remove preceeding '/'
    try:
        png = open(absolute, 'rb').read()
    except IOError:
        raise Http404
    return HttpResponse(png, content_type='image/png')

