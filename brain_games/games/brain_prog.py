import random
from brain_games.start_game import generate_rand_num


TASK = 'What number is missing in the progression?'


def module_func():
    gen_list = []
    num = generate_rand_num()
    step = generate_rand_num(1, 10)
    length = generate_rand_num(5, 10)
    for _ in range(length):
        gen_list.append(num)
        num += step
    rand_index = random.randint(0, length - 1)
    solution = str(gen_list[rand_index])
    num_expression = ' '.join(str(i).replace(solution, '..') for i in gen_list)
    return num_expression, solution
