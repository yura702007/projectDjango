from django import template
from .. import views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = views.cats_db
    return {'cats': cats}
