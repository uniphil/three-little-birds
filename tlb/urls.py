from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    # url(r'^tlb/', include('tlb.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^[\w\d\s\-\._]+\.txt$', 'root_static.views.txt'),
    url(r'^[\w\d\s\-\._]+\.png$', 'root_static.views.png'),
)
