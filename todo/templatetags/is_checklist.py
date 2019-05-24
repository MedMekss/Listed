from django import template

register = template.Library()


@register.filter
def is_checklist(items, checklist):
    return items.filter(checklist=checklist)
