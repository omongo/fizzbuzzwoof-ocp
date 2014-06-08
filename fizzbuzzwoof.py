import rules

class FizzBuzzWoofFactory:
    def create(self):
        return FizzBuzzWoof([rules.FizzBuzzWoof(), 
                             rules.BuzzWoof(),
                             rules.FizzWoof(),
                             rules.FizzBuzz(),
                             rules.Woof(),
                             rules.Buzz(),
                             rules.Fizz()])

class FizzBuzzWoof:
    def __init__(self, rules):
        self.rules = rules[:]
    def say(self, number):
        for rule in self.rules:
            if rule.is_valid(number):
                return rule.say()
        return str(number)
