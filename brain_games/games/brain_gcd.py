import math
from brain_games.start_game import generate_rand_num


TASK = 'Find the greatest common divisor of given numbers.'


def module_func():
    first_num = generate_rand_num(1, 100)
    second_num = generate_rand_num(1, 100)
    num_expression = f'{first_num} {second_num}'
    solution = str(math.gcd(first_num, second_num))
    return num_expression, solution
