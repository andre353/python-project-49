import random
from brain_games.start_game import generate_rand_num


def calc():
    game_name = 'brain_calc'
    first_num = generate_rand_num()
    second_num = generate_rand_num()
    list = ['+', '-', '*']
    operator = random.choice(list)
    string = f'{first_num} {operator} {second_num}'
    calculated_num = str(eval(string))
    return (string, calculated_num), game_name
