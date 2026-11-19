import unittest

from pagination import page, page_count


class PaginationTest(unittest.TestCase):
    def test_full_pages(self) -> None:
        self.assertEqual(page_count(9, 3), 3)
        self.assertEqual(page(list(range(1, 10)), 3, 3), [7, 8, 9])

    def test_first_page(self) -> None:
        self.assertEqual(page(list(range(1, 11)), 1, 3), [1, 2, 3])

    def test_last_partial_page(self) -> None:
        self.assertEqual(page_count(10, 3), 4)
        self.assertEqual(page(list(range(1, 11)), 4, 3), [10])


if __name__ == "__main__":
    unittest.main()
