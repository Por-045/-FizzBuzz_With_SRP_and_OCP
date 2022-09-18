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

    def test_give_6918_should_fizz(self):
        number = 6918
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

    def test_give_6785_should_buzz(self):
        number = 6785
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

    def test_give_9975_should_fizzbuzz(self):
        number = 9975
        excepted_result = 'FizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzModulusBy9Test(unittest.TestCase):
    def test_give_9_should_fizzfizz(self):
        number = 9
        excepted_result = 'FizzFizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_4572_should_fizzfizz(self):
        number = 4572
        excepted_result = 'FizzFizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_8181_should_fizzfizz(self):
        number = 8181
        excepted_result = 'FizzFizz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzModulusBy25Test(unittest.TestCase):
    def test_give_25_should_buzzbuzz(self):
        number = 25
        excepted_result = 'BuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_5075_should_buzzbuzz(self):
        number = 5075
        excepted_result = 'BuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_9725_should_buzzbuzz(self):
        number = 9725
        excepted_result = 'BuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzModulusBy9and25Test(unittest.TestCase):
    def test_give_225_should_fizzfizzbuzzbuzz(self):
        number = 225
        excepted_result = 'FizzFizzBuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_6750_should_fizzfizzbuzzbuzz(self):
        number = 6750
        excepted_result = 'FizzFizzBuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_9450_should_fizzfizzbuzzbuzz(self):
        number = 9450
        excepted_result = 'FizzFizzBuzzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzNotMetConditionTest(unittest.TestCase):
    def test_give_1_should_nofizzbuzz(self):
        number = 1
        excepted_result = 'NoFizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_4444_should_nofizzbuzzz(self):
        number = 4444
        excepted_result = 'NoFizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_9998_should_nofizzbuzz(self):
        number = 9998
        excepted_result = 'NoFizzBuzz'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

class FizzBuzzNotFrom0And10000Test(unittest.TestCase):
    def test_give_n1_should_notfrom0and10000(self):
        number = -1
        excepted_result = 'NotFrom0And10000'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_10001_should_notfrom0and10000(self):
        number = 10001
        excepted_result = 'NotFrom0And10000'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_n15_should_notfrom0and10000(self):
        number = -15
        excepted_result = 'NotFrom0And10000'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_30000_should_notfrom0and10000(self):
        number = 30000
        excepted_result = 'NotFrom0And10000'

        result = fizzbuzz(number)

        self.assertEqual(result, excepted_result)
