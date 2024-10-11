
from django import template
from django.utils import timezone
from datetime import datetime

register = template.Library()


@register.filter
def online_now(value):
    """Returns the difference between the current time and the given datetime in minutes."""
    if not isinstance(value, datetime):
        return 0
    now = timezone.now()
    delta = now - value
    # return delta.days * 24 * 60 + delta.seconds // 60
    return False if delta.days * 24 * 60 + delta.seconds // 60 > 0 else True