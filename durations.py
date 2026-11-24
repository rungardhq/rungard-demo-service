"""Format a run's length for the run list."""


def format_duration(seconds: int) -> str:
    """`seconds`, a non-negative whole number, as hours, minutes and seconds, e.g. 3723 -> "1h 02m 03s".

    Minutes and seconds are always two digits. Hours are omitted when zero,
    e.g. 65 -> "01m 05s".
    """
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    return f"{minutes:02d}m {secs:02d}s"
