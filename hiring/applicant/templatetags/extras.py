# applicant/templatetags/extras.py
import ast
from django import template

register = template.Library()

@register.filter
def parse_list(value):
    try:
        return ast.literal_eval(value)
    except:
        return []
