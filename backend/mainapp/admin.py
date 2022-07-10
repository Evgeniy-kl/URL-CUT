from django.contrib import admin

from mainapp.models import User, ShortUrl


@admin.register(User, ShortUrl)
class DefaultAdmin(admin.ModelAdmin):
    pass
