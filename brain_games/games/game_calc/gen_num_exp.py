import random
from brain_games.games.generate_rand_num import generate_rand_num


def gen_num_exp():
    first_num = generate_rand_num()
    second_num = generate_rand_num()
    list = ['+', '-', '*']
    operator = random.choice(list)
    string = f'{first_num} {operator} {second_num}'
    expr = string
    calculated_num = eval(expr)
    return string, str(calculated_num)
