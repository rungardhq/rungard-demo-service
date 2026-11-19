import unittest

from slugs import slugify


class SlugsTest(unittest.TestCase):
    def test_two_words(self) -> None:
        self.assertEqual(slugify("Hello World"), "hello-world")


if __name__ == "__main__":
    unittest.main()
