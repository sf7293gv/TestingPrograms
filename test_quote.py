import unittest
from unittest import TestCase
import quote


class QuoteTest(TestCase):
    
    def test_quote_for_small_lawn_sameday(self):
        actual_quote = quote.lawn_quote('small', True)
        expected_quote = 15
        self.assertEqual(expected_quote, actual_quote)

    def test_quote_for_large_lawn_notSameday(self):
        self.assertEqual(20, quote.lawn_quote('large', False))
    
    def test_quote_for_unrecognized(self):
        actual_quote = quote.lawn_quote('alligator', False)
        expected_quote = None
        self.assertIsNone(actual_quote)

if __name__ == '__main__':
    unittest.main()