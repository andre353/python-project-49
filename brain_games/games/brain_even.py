from brain_games.start_game import generate_rand_num


def even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    solution = ''
    num_expression = ''
    num_expression = str(generate_rand_num(1, 100))
    if (int(num_expression) % 2 == 0):
        solution = 'yes'
    else:
        solution = 'no'
    return (num_expression, solution), task
