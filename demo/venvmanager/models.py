"""
Models for the virtual env manager
"""

from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class VirtualEnv(models.Model):
    name = models.CharField(max_length=128)
    server = models.ForeignKey(Server)
    path = models.CharField(max_length=512)

    def __unicode__(self):
        return u'[%s] %s' % (self.server.name, self.name)


class Package(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return u'%s' % (self.name,)


class Version(models.Model):
    name = models.CharField(max_length=32)
    package = models.ForeignKey(Package)
    venv = models.ForeignKey(VirtualEnv)

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

    def package_name(self):
        return self.package.name
    package_name.admin_order_field = 'package__name'
