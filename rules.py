from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def is_valid(self, number):
        pass
    @abstractmethod
    def say(self, number):
        pass

class Number:
    def is_valid(self, number):
        return True
    def say(self, number):
        return str(number)

class Fizz:
    def is_valid(self, number):
        return number % 3 == 0
    def say(self, number):
        return 'Fizz'

class Buzz:
    def is_valid(self, number):
        return number % 5 == 0
    def say(self, number):
        return 'Buzz'

class Woof:
    def is_valid(self, number):
        return number % 7 == 0
    def say(self, number):
        return 'Woof'

class FizzBuzz:
    def is_valid(self, number):
        return number % 15 == 0
    def say(self, number):
        return 'FizzBuzz'

class FizzWoof:
    def is_valid(self, number):
        return number % 21 == 0
    def say(self, number):
        return 'FizzWoof'

class BuzzWoof:
    def is_valid(self, number):
        return number % 35 == 0
    def say(self, number):
        return 'BuzzWoof'

class FizzBuzzWoof:
    def is_valid(self, number):
        return number % 105 == 0
    def say(self, number):
        return 'FizzBuzzWoof'

Rule.register(Number)
Rule.register(Fizz)
Rule.register(Buzz)
Rule.register(Woof)
Rule.register(FizzBuzz)
Rule.register(FizzWoof)
Rule.register(BuzzWoof)
Rule.register(FizzBuzzWoof)
