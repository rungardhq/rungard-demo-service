import unittest

from emails import normalize_email


class EmailsTest(unittest.TestCase):
    def test_strips_whitespace(self) -> None:
        self.assertEqual(normalize_email("  ops@example.com "), "ops@example.com")

    def test_lower_cases_the_domain(self) -> None:
        self.assertEqual(normalize_email("ops@Example.COM"), "ops@example.com")

    def test_keeps_the_local_part_case(self) -> None:
        self.assertEqual(normalize_email("  John.Doe@Example.COM "), "John.Doe@example.com")
        self.assertEqual(normalize_email("a@b@Example.ORG"), "a@b@example.org")

    def test_address_without_at_is_only_stripped(self) -> None:
        self.assertEqual(normalize_email("  NoAt "), "NoAt")


if __name__ == "__main__":
    unittest.main()
