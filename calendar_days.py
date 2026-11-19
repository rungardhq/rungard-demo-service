"""Days in a month, for the service's monthly reports."""


def is_leap(year: int) -> bool:
    """Whether `year` is a leap year in the Gregorian calendar."""
    return year % 4 == 0


def days_in_month(year: int, month: int) -> int:
    """How many days `month` (1 to 12) of `year` has."""
    if not 1 <= month <= 12:
        raise ValueError(f"no month {month}")
    if month == 2:
        return 29 if is_leap(year) else 28
    return 30 if month in (4, 6, 9, 11) else 31
