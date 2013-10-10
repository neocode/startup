from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from poll import views

import pollurls

urlpatterns = patterns('',
                       url(r'^poll/', include(pollurls)),
                       url(r'^admin/', include(admin.site.urls)),
)