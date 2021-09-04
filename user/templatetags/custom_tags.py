from django import template

register = template.Library()

@register.filter
def per(a=0,b=0):
    return (a/b)*100
