from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'products.views.index'),
    url(r'^products/(?P<page>\d+)/$', 'products.views.home'),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^product/id=(?P<product_id>\d+)/$', 'products.views.view_product'),
    url(r'^page(?P<page>\d+)/$', 'products.views.page', name = 'home'),

    url(r'^time/json/$', 'products.views.timestamp'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
