import unittest

from billing import split_amount


class BillingTest(unittest.TestCase):
    def test_an_even_split(self) -> None:
        self.assertEqual(split_amount(900, 3), [300, 300, 300])

    def test_the_first_shares_take_the_extra_cents(self) -> None:
        self.assertEqual(split_amount(1000, 3), [334, 333, 333])


if __name__ == "__main__":
    unittest.main()
