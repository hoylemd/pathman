from django import template

register = template.Library()


@register.filter(name='modifier')
def modifier(value):
    try:
        mod = int(value)
    except ValueError:
        mod = None

    if mod is not None:
        return '%+d' % mod

    return '"{}" is not a valid modifier'.format(value)
