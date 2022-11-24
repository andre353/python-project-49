import random
import math


TASK = 'Find the greatest common divisor of given numbers.'


def get_expression_and_solution():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    expression = f'{first_num} {second_num}'
    solution = str(math.gcd(first_num, second_num))
    return expression, solution
