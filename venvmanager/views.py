"""
venvmanager.views
~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Linovia.
:license: BSD, see LICENSE for more details.
"""

import urllib

from venvmanager import models
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


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


#
# PACKAGES
#

FILTER_MAPPING = {
    'version': 'name__exact',
    'package_id': 'package_id__in',
    'venv_id': 'venv_id__in',
    'server_id': 'venv__server_id__in',
}


class PackageList(ListView):
    model = models.Version
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        # TODO: use redirect & merge the GET and POST arguments
        filters = {}
        for arg in FILTER_MAPPING:
            if arg in self.request.REQUEST.keys():
                filters[arg] = ','.join(self.request.REQUEST.getlist(arg))
        return redirect(request.path + '?' + urllib.urlencode(filters))

    def convert_filter(self, key):
        filter_name = FILTER_MAPPING[key]
        self.filters[filter_name] = self.request.REQUEST.getlist(key)

        # If list size is 1 then it isn't a list
        if len(self.filters[filter_name]) == 1:
            self.filters[filter_name] = self.filters[filter_name][0]

        # If we have a string list, make it a real list
        if filter_name[-4:] == '__in' and \
            not isinstance(self.filters[filter_name], (list, tuple)):
            self.filters[filter_name] = self.filters[filter_name].split(',')

        # Try to cast the list items to integers
        try:
            values = []
            if isinstance(self.filters[filter_name], (list, tuple)):
                for item in self.filters[filter_name]:
                    values.append(int(item))
            self.filters[filter_name] = values
        except:
            pass
        return {filter_name: self.filters[filter_name]}

    def get_queryset(self):
        kwargs = {}
        self.filters = {}
        for arg in FILTER_MAPPING:
            if arg in self.request.REQUEST.keys():
                kwargs.update(self.convert_filter(arg))

        return models.Version.objects.filter(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(PackageList, self).get_context_data(**kwargs)
        context['servers'] = models.Server.objects.all().order_by('name')
        context['venvs'] = models.VirtualEnv.objects.all().order_by('name')
        context['packages'] = models.Package.objects.all().order_by('name')
        context['filters'] = self.filters
        for key, value in list(context['filters'].iteritems()):
            if key[-4:] == '__in':
                context['filters'][key[:-4]] = value
                del context['filters'][key]
        return context


class PackageDetail(DetailView):
    model = models.Package
    pk_url_kwarg = 'package_id'


from django.contrib.auth.decorators import login_required


@login_required
def update_venvs(request):
    from fabric.api import env, run

    env.user = 'ordoquy'
    for venv in models.VirtualEnv.objects.all():
        env.host_string = venv.server.full_name
        results = run('source %s/bin/activate; pip freeze -l 2>/dev/null' % venv.path)
        for result in results.split('\n'):
            if result[0:2] == '##':
                continue
            if '==' not in result:
                print 'TODO:', result
                continue
            result = result.strip('\r')
            package_name, version_name = result.split('==')
            package, created = models.Package.objects.get_or_create(name=package_name)
            version, created = models.Version.objects.get_or_create(
                package=package,
                venv=venv
            )
            if created or version.name != version_name:
                version.name = version_name
                version.save()

    return redirect('packages')
