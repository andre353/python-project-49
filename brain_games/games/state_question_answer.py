import math
from brain_games.games.generate_rand_num import generate_rand_num
from brain_games.games.generate_num_expression import generate_num_expression
from brain_games.games.generate_progression import generate_progression
from brain_games.games.check_if_prime import check_if_prime


def state_question_answer(game):
    right_answer = ''
    num_expression = ''
    if (game == 'brain_even'):
        num_expression = str(generate_rand_num())
        if (int(num_expression) % 2 == 0):
            right_answer = 'yes'
        else:
            right_answer = 'no'
    elif (game == 'brain_calc'):
        num_expression, right_answer = generate_num_expression()
    elif (game == 'brain_gcd'):
        first_num = generate_rand_num()
        second_num = generate_rand_num()
        num_expression = f'{first_num} {second_num}'
        right_answer = str(math.gcd(first_num, second_num))
    elif (game == 'brain_progression'):
        num_expression, right_answer = generate_progression()
    elif (game == 'brain_prime'):
        prep_num = generate_rand_num()
        right_answer = check_if_prime(prep_num)
        num_expression = str(prep_num)
    return num_expression, right_answer
