from django.contrib import admin

from pythons.pythons_app.models import Python


class PythonsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Python, PythonsAdmin)