from brain_games.games.generate_rand_num import generate_rand_num


def brain_even_qa():
    right_answer = ''
    num_expression = ''
    num_expression = str(generate_rand_num())
    if (int(num_expression) % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return num_expression, right_answer
