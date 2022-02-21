from django.contrib import admin

from .models import Beer, Photo

admin.site.register(Beer)
admin.site.register(Photo)