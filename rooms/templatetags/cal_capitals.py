from django import template

register = template.Library()


@register.filter()
def cal_capitals(value):
    return value.capitalize()