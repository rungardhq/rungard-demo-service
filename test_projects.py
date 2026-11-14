import unittest

from projects import get_project


class ProjectsTest(unittest.TestCase):
    def test_a_known_project(self) -> None:
        self.assertEqual(get_project("/projects/alpha"), (200, {"id": "alpha", "name": "Alpha"}))


if __name__ == "__main__":
    unittest.main()
