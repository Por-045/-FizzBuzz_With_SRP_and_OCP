from src.fizzbuzz import fizzbuzz
import unittest

class FizzBuzzModulusBy3Test(unittest.TestCase):
    def test_give_3_should_fizz(self):
        number = 3
        excepted_result = 'Fizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_1596_should_fizz(self):
        number = 1596
        excepted_result = 'Fizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_6921_should_fizz(self):
        number = 6921
        excepted_result = 'Fizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzModulusBy5Test(unittest.TestCase):
    def test_give_5_should_buzz(self):
        number = 5
        excepted_result = 'Buzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_9985_should_buzz(self):
        number = 9985
        excepted_result = 'Buzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_6775_should_buzz(self):
        number = 6775
        excepted_result = 'Buzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzModulusBy3and5Test(unittest.TestCase):
    def test_give_15_should_fizzbuzz(self):
        number = 15
        excepted_result = 'FizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_6015_should_fizzbuzz(self):
        number = 6015
        excepted_result = 'FizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_9990_should_fizzbuzz(self):
        number = 9990
        excepted_result = 'FizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)
