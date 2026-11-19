"""Turn a project name into the slug used in its URL."""


def slugify(name: str) -> str:
    """The URL slug of `name`: lower case, words joined by single hyphens."""
    return name.lower().replace(" ", "-")
