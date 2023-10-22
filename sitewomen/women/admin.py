from django.contrib import admin
from .models import Women, Category


# Register your models here.
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'cat')
    list_per_page = 5
    ordering = ['time_create', 'title']
    search_fields = ['title__startswith', 'cat__name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
