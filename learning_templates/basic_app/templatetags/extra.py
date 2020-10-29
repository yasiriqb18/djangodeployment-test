from django import template

register= template.Library()

@register.filter(name='cut')
def cut(value, args):

    """
    this cuts out all the values of arg fromt eh strings

    """

    return value.replace(args,'')

#register.filter('cut',cut)

