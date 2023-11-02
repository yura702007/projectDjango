from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Семейное положение'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'cat', 'photo', 'content', 'husband']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'cat')
    list_per_page = 5
    ordering = ['time_create', 'title']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Изображение")
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Без фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
