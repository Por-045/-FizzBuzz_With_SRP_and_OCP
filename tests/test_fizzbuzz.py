from src.fizzbuzz import fizzbuzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_fizz(self):
        number = 3
        excepted_result = 'Fizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)