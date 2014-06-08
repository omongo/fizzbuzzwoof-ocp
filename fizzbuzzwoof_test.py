import unittest

from fizzbuzzwoof import FizzBuzzWoofFactory

class TestFizzBuzz(unittest.TestCase):

    def test_1_should_be_1(self):
        expected = '1'
        actual = FizzBuzzWoofFactory().create().say(1)
        self.assertEqual(expected, actual)

    def test_3_should_be_Fizz(self):
        expected = 'Fizz'
        actual = FizzBuzzWoofFactory().create().say(3)
        self.assertEqual(expected, actual)

    def test_5_should_be_Buzz(self):
        expected = 'Buzz'
        actual = FizzBuzzWoofFactory().create().say(5)
        self.assertEqual(expected, actual)

    def test_7_should_be_Woof(self):
        expected = 'Woof'
        actual = FizzBuzzWoofFactory().create().say(7)
        self.assertEqual(expected, actual)

    def test_15_should_be_FizzBuzz(self):
        expected = 'FizzBuzz'
        actual = FizzBuzzWoofFactory().create().say(15)
        self.assertEqual(expected, actual)

    def test_21_should_be_FizzWoof(self):
        expected = 'FizzWoof'
        actual = FizzBuzzWoofFactory().create().say(21)
        self.assertEqual(expected, actual)

    def test_35_should_be_BuzzWoof(self):
        expected = 'BuzzWoof'
        actual = FizzBuzzWoofFactory().create().say(35)
        self.assertEqual(expected, actual)

    def test_105_should_be_FizzBuzzWoof(self):
        expected = 'FizzBuzzWoof'
        actual = FizzBuzzWoofFactory().create().say(105)
        self.assertEqual(expected, actual)

