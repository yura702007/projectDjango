from django import template
from .. import views
from ..models import Category

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
