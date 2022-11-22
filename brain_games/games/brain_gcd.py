import math
from brain_games.start_game import generate_rand_num


def gcd():
    task = 'Find the greatest common divisor of given numbers.'
    first_num = generate_rand_num(1, 100)
    second_num = generate_rand_num(1, 100)
    num_expression = f'{first_num} {second_num}'
    solution = str(math.gcd(first_num, second_num))
    return (num_expression, solution), task
