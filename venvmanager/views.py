"""
venvmanager.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from . import models
from django.views.generic import ListView, UpdateView, DetailView, CreateView


class ServerList(ListView):
    model = models.Server


class ServerDetail(DetailView):
    model = models.Server


class ServerUpdate(UpdateView):
    model = models.Server


class ServerNew(CreateView):
    model = models.Server


class VirtualEnvList(ListView):
    model = models.VirtualEnv
