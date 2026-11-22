import unittest

from durations import format_duration


class DurationsTest(unittest.TestCase):
    def test_hours_minutes_seconds(self) -> None:
        self.assertEqual(format_duration(3 * 3600 + 25 * 60 + 47), "3h 25m 47s")


if __name__ == "__main__":
    unittest.main()
