from django.conf.urls import patterns, include, url
from tlb import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^bio$', 'pages.views.bio', name='bio'),
    url(r'^gallery$', 'pages.views.gallery', name='gallery'),
    url(r'^media$', 'pages.views.media', name='media'),
    url(r'^store$', 'pages.views.store', name='store'),
    url(r'^contact$', 'pages.views.contact', name='contact'),

    # url(r'^tlb/', include('tlb.foo.urls')),
    url(r'^soundmanager2.swf', 'pages.views.sm2', name='sm2'),
    url(r'^crossdomain.xml$', 'pages.views.crossdomain', name='xdomain'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^[\w\d\s\-\._]+\.txt$', 'root_static.views.txt'),
    url(r'^[\w\d\s\-\._]+\.png$', 'root_static.views.png'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
