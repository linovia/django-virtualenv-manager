"""
venvmanager.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

from . import models
from django.views.generic import ListView


class ServerList(ListView):
    model = models.Server


class VirtualEnvList(ListView):
    model = models.VirtualEnv
