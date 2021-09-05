from django import template

register = template.Library()


def per(a,b):
    return (a/b)*100
