class Question:
    answer = None
    text = None


class Add(Question):
    def __init__(self, num_1, num_2):
        self.text = '{} + {}'.format(num_1, num_2)
        self.answer = num_1 + num_2


class Multiply(Question):
    def __init__(self, num_1, num_2):
        self.text = '{} x {}'.format(num_1, num_2)
        self.answer = num_1 * num_2
