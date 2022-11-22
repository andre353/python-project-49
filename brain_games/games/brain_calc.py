import random
from brain_games.start_game import generate_rand_num


def calc():
    task = 'What is the result of the expression?'
    first_num = generate_rand_num()
    second_num = generate_rand_num()
    list = ['+', '-', '*']
    operator = random.choice(list)
    num_expression = f'{first_num} {operator} {second_num}'
    solution = str(eval(num_expression))
    num_expression, solution
    return (num_expression, solution), task
