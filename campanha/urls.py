from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'campanha.views.home', name='home'),
    # url(r'^campanha/', include('campanha.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
urlpatterns += patterns(
    'django.views.static', url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
)