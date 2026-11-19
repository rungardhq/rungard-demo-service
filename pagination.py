"""Split a list of items into numbered pages."""


def page_count(total: int, size: int) -> int:
    """How many pages `total` items fill, `size` to a page."""
    if size < 1:
        raise ValueError("size must be at least 1")
    return -(-total // size)


def page(items: list, number: int, size: int) -> list:
    """The items on page `number`, counted from 1."""
    if not 1 <= number <= page_count(len(items), size):
        raise IndexError(f"no page {number}")
    start = (number - 1) * size
    return items[start : start + size]
