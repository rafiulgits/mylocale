from django import template
from django.template import Template
from farmer.models import FOOD_CATEGORY_DIC

register = template.Library()

@register.filter(name='cat')
def crop_category(code):
    return FOOD_CATEGORY_DIC[code]