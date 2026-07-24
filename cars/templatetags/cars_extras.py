import datetime

from django import template

from cars.models import Car

register = template.Library()


@register.simple_tag
def site_name():
    """Sayt nomini chiqaradi (talab 8)"""
    return "AutoMarket"


@register.simple_tag
def current_year():
    """Joriy yilni chiqaradi (talab 8)"""
    return datetime.date.today().year


@register.simple_tag
def total_cars_count():
    """Bazadagi umumiy mashinalar sonini chiqaradi (talab 8)"""
    return Car.objects.count()
