from django.contrib import admin
from .models import Server, VirtualEnv, Package, Version

from fabric.api import env, run


def check_virtual_env(modeladmin, request, queryset):
    env.user = 'ordoquy'
    for venv in queryset:
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
            package, created = Package.objects.get_or_create(name=package_name)
            version, created = Version.objects.get_or_create(
                package=package,
                venv=venv
            )
            if created or version.name != version_name:
                version.name = version_name
                version.save()

check_virtual_env.short_description = "Update the virtual env."


class ServerAdmin(admin.ModelAdmin):
    pass


class VirtualEnvAdmin(admin.ModelAdmin):
    actions = [check_virtual_env]


class PackageAdmin(admin.ModelAdmin):
    pass


class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'package_name', 'venv_name', 'server_name')
    list_filter = ('package', 'venv')


admin.site.register(Server, ServerAdmin)
admin.site.register(VirtualEnv, VirtualEnvAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Version, VersionAdmin)
