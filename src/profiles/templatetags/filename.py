# coding=utf-8
from django import template
import os

register = template.Library()

@register.filter(name="filename")
def filename(value, *args):
    return os.path.basename(value)

#register.filter('filename', filename)