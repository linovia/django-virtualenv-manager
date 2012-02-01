"""
venvmanager.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from . import models
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy


#
# SERVERS SECTION
#

class ServerList(ListView):
    model = models.Server


class ServerNew(CreateView):
    model = models.Server
    success_url = reverse_lazy('servers')


class ServerDetail(DetailView):
    model = models.Server
    pk_url_kwarg = 'server_id'


class ServerUpdate(UpdateView):
    model = models.Server
    pk_url_kwarg = 'server_id'
    success_url = reverse_lazy('servers')


class ServerDelete(DeleteView):
    model = models.Server
    pk_url_kwarg = 'server_id'
    success_url = reverse_lazy('servers')


#
# VIRTUALENVS
#

class VenvList(ListView):
    model = models.VirtualEnv


class VenvNew(CreateView):
    model = models.VirtualEnv
    success_url = reverse_lazy('venvs')


class VenvDetail(DetailView):
    model = models.VirtualEnv
    pk_url_kwarg = 'venv_id'


class VenvUpdate(UpdateView):
    model = models.VirtualEnv
    pk_url_kwarg = 'venv_id'
    success_url = reverse_lazy('venvs')


class VenvDelete(DeleteView):
    model = models.VirtualEnv
    pk_url_kwarg = 'venv_id'
    success_url = reverse_lazy('venvs')
