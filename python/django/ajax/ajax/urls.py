from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^$', 'app.views.index', name='home'),

    url(r'^ajax_list/$', 'app.views.ajax_list', name='ajax-list'),
    url(r'^ajax_dict/$', 'app.views.ajax_dict', name='ajax-dict'),
    url(r'^ajax_add/$', 'app.views.ajax_add', name='ajax-add'),
    url(r'^sendmail/$', 'app.views.sendmail', name='sendmail'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^app/', include('app.urls')),

    # url(r'^so/(?P<required>\d+)/(?P<optional>.*)/$', 'myapp.so', name='something_else')
)
