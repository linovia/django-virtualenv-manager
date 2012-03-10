"""
venvmanager.urls
~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls.defaults import patterns, url, include
from . import views

server_urlpatterns = patterns('',
    url(r'^$',                              views.ServerList.as_view(),     name='servers'),
    url(r'^new/$',                          views.ServerNew.as_view(),      name='server-new'),
    url(r'^(?P<server_id>\d+)/$',           views.ServerDetail.as_view(),   name='server-detail'),
    url(r'^(?P<server_id>\d+)/update/$',    views.ServerUpdate.as_view(),   name='server-update'),
    url(r'^(?P<server_id>\d+)/delete/$',    views.ServerDelete.as_view(),   name='server-delete'),
)

venv_urlpatterns = patterns('',
    url(r'^$',                              views.VenvList.as_view(),       name='venvs'),
    url(r'^new/$',                          views.VenvNew.as_view(),        name='venv-new'),
    url(r'^(?P<venv_id>\d+)/$',             views.VenvDetail.as_view(),     name='venv-detail'),
    url(r'^(?P<venv_id>\d+)/update/$',      views.VenvUpdate.as_view(),     name='venv-update'),
    url(r'^(?P<venv_id>\d+)/delete/$',      views.VenvDelete.as_view(),     name='venv-delete'),

    url(r'^update/$',                       views.update_venvs,             name='update-all-venvs'),
)

package_urlpatterns = patterns('',
    url(r'^$',                              views.PackageList.as_view(),    name='packages'),
    url(r'^(?P<package_id>\d+)/$',           views.PackageDetail.as_view(),  name='package-detail'),
)

urlpatterns = patterns('',
    url(r'^servers/',   include(server_urlpatterns)),
    url(r'^envs/',      include(venv_urlpatterns)),
    url(r'^packages/',  include(package_urlpatterns)),
)
