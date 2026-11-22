import unittest

from emails import normalize_email


class EmailsTest(unittest.TestCase):
    def test_strips_whitespace(self) -> None:
        self.assertEqual(normalize_email("  ops@example.com "), "ops@example.com")

    def test_lower_cases_the_domain(self) -> None:
        self.assertEqual(normalize_email("ops@Example.COM"), "ops@example.com")


if __name__ == "__main__":
    unittest.main()
