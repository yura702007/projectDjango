from django.contrib import admin
from .models import Women


# Register your models here.
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['time_create', 'title']
