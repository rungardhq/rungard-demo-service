import unittest

from calendar_days import days_in_month


class CalendarDaysTest(unittest.TestCase):
    def test_february(self) -> None:
        self.assertEqual(days_in_month(2024, 2), 29)
        self.assertEqual(days_in_month(2023, 2), 28)

    def test_long_and_short_months(self) -> None:
        self.assertEqual(days_in_month(2023, 1), 31)
        self.assertEqual(days_in_month(2023, 4), 30)


if __name__ == "__main__":
    unittest.main()
