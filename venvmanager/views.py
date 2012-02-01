"""
venvmanager.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from . import models
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class ServerList(ListView):
    model = models.Server


class ServerDetail(DetailView):
    model = models.Server
    pk_url_kwarg = 'server_id'


class ServerUpdate(UpdateView):
    model = models.Server
    pk_url_kwarg = 'server_id'
    success_url = reverse_lazy('servers')


class ServerNew(CreateView):
    model = models.Server
    success_url = reverse_lazy('servers')


class ServerDelete(DeleteView):
    model = models.Server


class VirtualEnvList(ListView):
    model = models.VirtualEnv
