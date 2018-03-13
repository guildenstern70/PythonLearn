

from .learnobject import LearnObject


class Comprehensions:

    def __init__(self):
        self.items = ['apple', 'ananas', 'banana', 'mango']
        self.numbers = [1, 2, 3, 4, 5]
        self.new_numbers = []
        self.new_strings = []

    def list_comprehension(self):
        self.new_numbers = [n*2 for n in self.numbers]
        self.new_strings = [s.upper() for s in self.items if s.startswith('a')]

    def output(self):
        self.list_comprehension()
        LearnObject.print_collection('COMPREHENSION', self.new_numbers)
        LearnObject.print_collection('COMPREHENSION', self.new_strings)
