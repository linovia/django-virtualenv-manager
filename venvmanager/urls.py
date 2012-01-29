"""
venvmanager.urls
~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls.defaults import patterns, url, include
from . import views

servers_urlpatterns = patterns('',
    url(r'^$',                      views.ServerList.as_view(),     name='servers'),
    url(r'^new/$',                  views.ServerNew.as_view(),      name='server-new'),
    url(r'^(?P<id>\d+)/$',          views.ServerDetail.as_view(),   name='server-detail'),
    url(r'^(?P<id>\d+)/update/$',   views.ServerUpdate.as_view(),   name='server-update'),
)

urlpatterns = patterns('',
    url(r'^servers/', include(servers_urlpatterns)),
    url(r'^envs/$', views.VirtualEnvList.as_view(), name='environments'),
)
