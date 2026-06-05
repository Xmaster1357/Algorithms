import unittest
from shortener import URLShortener


class TestURLShortener(unittest.TestCase):

    def setUp(self):
        self.shortener = URLShortener()

    def test_add_link(self):
        code = self.shortener.add_link(
            "https://example.com"
        )

        self.assertTrue(
            self.shortener.exists(code)
        )

    def test_get_link(self):
        code = self.shortener.add_link(
            "https://example.com"
        )

        url = self.shortener.get_link(code)

        self.assertEqual(
            url,
            "https://example.com"
        )

    def test_exists(self):
        code = self.shortener.add_link(
            "https://example.com"
        )

        self.assertTrue(
            self.shortener.exists(code)
        )

        self.assertFalse(
            self.shortener.exists("abcd")
        )

    def test_click_counter(self):
        code = self.shortener.add_link(
            "https://example.com"
        )

        self.shortener.get_link(code)
        self.shortener.get_link(code)
        self.shortener.get_link(code)

        self.assertEqual(
            self.shortener.get_clicks(code),
            3
        )


if __name__ == "__main__":
    unittest.main()