"""Answer GET /projects/<id>."""

PROJECTS = {"alpha": {"id": "alpha", "name": "Alpha"}, "beta": {"id": "beta", "name": "Beta"}}


def get_project(path: str) -> tuple[int, dict | None]:
    """The status code and the JSON body of GET `path`."""
    project_id = path.removeprefix("/projects/")
    return 200, PROJECTS.get(project_id)
