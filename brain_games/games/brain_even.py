from brain_games.start_game import generate_rand_num


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def module_func():
    solution = ''
    num_expression = ''
    num_expression = str(generate_rand_num(1, 100))
    if (int(num_expression) % 2 == 0):
        solution = 'yes'
    else:
        solution = 'no'
    return num_expression, solution
