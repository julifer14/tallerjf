from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cotxes.views.home', name='home'),
    url(r'^cotxes/', include('cotxes.urls', namespace="cotxesns")),
    url(r'^admin/', include(admin.site.urls)),
)
