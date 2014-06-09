import rules

class FizzBuzzWoofFactory:
    def create(self):
        return FizzBuzzWoof([rules.Fizz(), rules.Buzz(), rules.Woof()])

class FizzBuzzWoof:
    def __init__(self, rules):
        self._rules = rules[:]
    def say(self, number):
        word = ''
        for rule in self._rules:
            word += rule.syllable * rule.is_valid(number)
        return word or str(number)

