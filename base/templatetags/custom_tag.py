from django import template
register = template.Library()

@register.filter
def reverselist(value):
  reversed_list = value[::-1]
  return reversed_list

@register.filter
def description(value):
  first = value[:200]
  return first+"..."