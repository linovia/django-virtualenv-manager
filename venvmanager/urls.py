"""
venvmanager.urls
~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls.defaults import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^servers/$',  views.ServerList.as_view(),         name='servers'),
    url(r'^envs/$',     views.VirtualEnvList.as_view(),     name='environments'),
)
