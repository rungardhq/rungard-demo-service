import unittest

from billing import split_amount


class BillingTest(unittest.TestCase):
    def test_an_even_split(self) -> None:
        self.assertEqual(split_amount(900, 3), [300, 300, 300])


if __name__ == "__main__":
    unittest.main()
