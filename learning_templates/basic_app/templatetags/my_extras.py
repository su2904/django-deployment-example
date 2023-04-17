from django import template
register = template.Library()

@register.filter(name='add')
def add(value,arg):
    return value + arg
# @register.filter(name='add_value')
# def add_value(value,arg):

#     return (value + arg)

# register.filter('cut',cut)

@register.filter()
def toupper(value):
    return value.upper()