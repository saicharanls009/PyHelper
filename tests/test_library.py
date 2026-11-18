
import unittest

from pyhelper.math_utils import factorial, is_prime
from pyhelper.string_utils import reverse_text, is_palindrome, count_words
from pyhelper.date_utils import is_leap_year, days_between, get_weekday


class TestMathUtilities(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_prime_number(self):
        self.assertTrue(is_prime(7))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(10))


class TestStringUtilities(unittest.TestCase):

    def test_reverse_text(self):
        self.assertEqual(reverse_text("Python"), "nohtyP")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_word_count(self):
        self.assertEqual(count_words("Python is easy"), 3)


class TestDateUtilities(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2024))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2025))

    def test_days_between(self):
        self.assertEqual(
            days_between("2026-01-01", "2026-01-11"), 10
        )

    def test_weekday(self):
        self.assertEqual(get_weekday("2026-11-18"), "Wednesday")


if __name__ == "__main__":
    unittest.main()
