"""Turn a project name into the slug used in its URL."""


def slugify(name: str) -> str:
    """The URL slug of `name`: lower case, words joined by single hyphens.

    Words are separated by runs of whitespace. Other characters are kept as they are.
    """
    return "-".join(name.lower().split())
