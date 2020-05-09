from django import template

register = template.Library()

@register.filter(name = 'taie')
def cut(value, arg):
    return value.replace(arg, '')
