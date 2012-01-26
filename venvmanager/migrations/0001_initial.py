# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Server'
        db.create_table('venvmanager_server', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('venvmanager', ['Server'])

        # Adding model 'VirtualEnv'
        db.create_table('venvmanager_virtualenv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venvmanager.Server'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('venvmanager', ['VirtualEnv'])

        # Adding model 'Package'
        db.create_table('venvmanager_package', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('venvmanager', ['Package'])

        # Adding model 'Version'
        db.create_table('venvmanager_version', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venvmanager.Package'])),
            ('venv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venvmanager.VirtualEnv'])),
        ))
        db.send_create_signal('venvmanager', ['Version'])


    def backwards(self, orm):
        
        # Deleting model 'Server'
        db.delete_table('venvmanager_server')

        # Deleting model 'VirtualEnv'
        db.delete_table('venvmanager_virtualenv')

        # Deleting model 'Package'
        db.delete_table('venvmanager_package')

        # Deleting model 'Version'
        db.delete_table('venvmanager_version')


    models = {
        'venvmanager.package': {
            'Meta': {'object_name': 'Package'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'venvmanager.server': {
            'Meta': {'object_name': 'Server'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'venvmanager.version': {
            'Meta': {'object_name': 'Version'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['venvmanager.Package']"}),
            'venv': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['venvmanager.VirtualEnv']"})
        },
        'venvmanager.virtualenv': {
            'Meta': {'object_name': 'VirtualEnv'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['venvmanager.Server']"})
        }
    }

    complete_apps = ['venvmanager']
