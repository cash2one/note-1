from django.conf.urls import patterns, include, url
from django.contrib import admin
from getjson.views import get_spider

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ijson.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get-spider-json/', get_spider),

    url(r'^admin/', include(admin.site.urls)),
)
