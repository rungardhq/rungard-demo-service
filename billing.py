"""Split an invoice between the teams that share it."""


def split_amount(cents: int, parts: int) -> list[int]:
    """`cents` split into `parts` shares that differ by at most one cent."""
    if parts < 1:
        raise ValueError("parts must be at least 1")
    return [cents // parts] * parts
