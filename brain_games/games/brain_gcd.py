import math
from brain_games.start_game import generate_rand_num


def gcd():
    game_name = 'brain_gcd'
    first_num = generate_rand_num(1, 100)
    second_num = generate_rand_num(1, 100)
    num_expression = f'{first_num} {second_num}'
    right_answer = str(math.gcd(first_num, second_num))
    return (num_expression, right_answer), game_name
