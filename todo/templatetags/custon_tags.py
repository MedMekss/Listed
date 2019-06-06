import math
from django import template

register = template.Library()


@register.filter
def is_checklist(items, checklist):
    return items.filter(checklist=checklist)


@register.filter
def get_progress(items, checklist):
    item = items.filter(checklist=checklist)
    checked = item.filter(completed=True)
    output = 0
    try:
        output = int(len(checked) / len(item) * 100)
    finally:
        return output
