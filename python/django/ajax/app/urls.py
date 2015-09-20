from django.conf.urls import patterns, include, url
from views import testurl


urlpatterns = patterns('',

    url(r'^urltest/$', testurl),

)
