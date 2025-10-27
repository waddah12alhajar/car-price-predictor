"""Utility functions for feature transformation."""
from datetime import datetime


def car_age(manufacturing_year):
    """Calculate car age based on manufacturing year."""
    current_year = datetime.now().year
    return current_year - manufacturing_year


def old_or_new(age):
    """Classify car as old or new based on age."""
    return 'New' if age < 15 else 'Old'


def car_usage_level(driven_per_year):
    """Classify car usage level based on miles driven per year."""
    if driven_per_year >= 5000:
        return 'Highly Driven'
    elif 1000 <= driven_per_year < 5000:
        return 'Moderately Driven'
    else:
        return 'Less Driven'


def state_level(value):
    """Classify state importance level."""
    if value >= 100000:
        return 'High'
    elif 50000 <= value < 100000:
        return 'Moderate'
    else:
        return 'Less'


def city_level(value):
    """Classify city importance level."""
    if value >= 10000:
        return 'High'
    elif 1000 <= value < 10000:
        return 'Moderate'
    else:
        return 'Less'
