class Fizz:
    def is_valid(self, number):
        return number % 3 == 0
    def say(self):
        return 'Fizz'

class Buzz:
    def is_valid(self, number):
        return number % 5 == 0
    def say(self):
        return 'Buzz'

class Woof:
    def is_valid(self, number):
        return number % 7 == 0
    def say(self):
        return 'Woof'

class FizzBuzz:
    def is_valid(self, number):
        return number % 15 == 0
    def say(self):
        return 'FizzBuzz'

class FizzWoof:
    def is_valid(self, number):
        return number % 21 == 0
    def say(self):
        return 'FizzWoof'

class BuzzWoof:
    def is_valid(self, number):
        return number % 35 == 0
    def say(self):
        return 'BuzzWoof'

class FizzBuzzWoof:
    def is_valid(self, number):
        return number % 105 == 0
    def say(self):
        return 'FizzBuzzWoof'

