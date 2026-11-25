import unittest

from retries import backoff_delays


class RetriesTest(unittest.TestCase):
    def test_doubles_from_base(self) -> None:
        self.assertEqual(backoff_delays(3, 1, 100), [1, 2, 4])

    def test_caps_at_maximum(self) -> None:
        delays = backoff_delays(5, 1, 10)
        self.assertEqual(delays, [1.0, 2.0, 4.0, 8.0, 10.0])
        self.assertTrue(all(isinstance(d, float) for d in delays))


if __name__ == "__main__":
    unittest.main()
