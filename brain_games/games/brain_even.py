import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_expression_and_solution():
    expression = random.randint(0, 100)
    solution = 'yes' if (expression) % 2 == 0 else 'no'
    return expression, solution
