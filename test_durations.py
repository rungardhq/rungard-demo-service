import unittest

from durations import format_duration


class DurationsTest(unittest.TestCase):
    def test_hours_minutes_seconds(self) -> None:
        self.assertEqual(format_duration(3 * 3600 + 25 * 60 + 47), "3h 25m 47s")

    def test_pads_minutes_and_seconds(self) -> None:
        self.assertEqual(format_duration(3723), "1h 02m 03s")

    def test_under_an_hour(self) -> None:
        self.assertEqual(format_duration(65), "01m 05s")

    def test_zero(self) -> None:
        self.assertEqual(format_duration(0), "00m 00s")


if __name__ == "__main__":
    unittest.main()
