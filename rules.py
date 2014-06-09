from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def is_valid(self):
        pass
    @property
    def syllable(self):
        return self._syllable
    @syllable.setter
    def syllable(self, val):
        self._syllable = val

class Fizz(Rule):
    def __init__(self):
        self._syllable = 'Fizz'
    def is_valid(self, number):
        return number % 3 == 0

class Buzz(Rule):
    def __init__(self):
        self._syllable = 'Buzz'
    def is_valid(self, number):
        return number % 5 == 0

class Woof(Rule):
    def __init__(self):
        self._syllable = 'Woof'
    def is_valid(self, number):
        return number % 7 == 0

