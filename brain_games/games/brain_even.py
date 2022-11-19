from brain_games.start_game import generate_rand_num


def even():
    game_name = 'brain_even'
    right_answer = ''
    num_expression = ''
    num_expression = str(generate_rand_num(1, 100))
    if (int(num_expression) % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (num_expression, right_answer), game_name
