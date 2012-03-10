"""
Models for the virtual env manager
"""

from django.db import models
from django.core.urlresolvers import reverse_lazy


class Server(models.Model):
    name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('server-detail', args=[self.id])


class VirtualEnv(models.Model):
    name = models.CharField(max_length=128)
    server = models.ForeignKey(Server)
    path = models.CharField(max_length=512)

    def __unicode__(self):
        return u'[%s] %s' % (self.server.name, self.name)

    def get_absolute_url(self):
        return reverse_lazy('venv-detail', args=[self.id])


class Package(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return u'%s' % (self.name,)


class Version(models.Model):
    name = models.CharField(max_length=32)
    package = models.ForeignKey(Package, related_name='versions')
    venv = models.ForeignKey(VirtualEnv, related_name='versions')

    def __unicode__(self):
        return u'[%s:%s] %s %s' % (
            self.venv.server.name,
            self.venv.name,
            self.package.name,
            self.name
        )

    def venv_name(self):
        return self.venv.name
    venv_name.admin_order_field = 'venv__name'

    def server_name(self):
        return self.venv.server.name
    venv_name.admin_order_field = 'venv__server__name'

    def package_name(self):
        return self.package.name
    package_name.admin_order_field = 'package__name'
