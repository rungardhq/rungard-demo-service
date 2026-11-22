import unittest

from retries import backoff_delays


class RetriesTest(unittest.TestCase):
    def test_doubles_from_base(self) -> None:
        self.assertEqual(backoff_delays(3, 1, 100), [1, 2, 4])


if __name__ == "__main__":
    unittest.main()
