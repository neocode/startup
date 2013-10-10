from django.conf.urls import patterns, url

from poll import views

urlpatterns = patterns('',
                            # ex: /poll/
                           url(r'^$', views.index, name='index'),
                           # ex: /poll/5/
                           url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                           # ex: /poll/5/results/
                           url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
                           # ex: /poll/5/vote/
                           url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)