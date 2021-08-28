from django import template
from stena.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

# @register.inclusion_tag('ссылка на html шаблон с фрагментом разметки') - декоратор рендера шаблона
# def show_categories():
#     categories = Category.objects.all()
#     return {"categories": categories}
