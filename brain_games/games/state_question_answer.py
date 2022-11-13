from brain_games.games.game_progression.gen_prog import gen_prog
from brain_games.games.game_calc.gen_num_exp import gen_num_exp
from brain_games.games.game_even.brain_even_qa import brain_even_qa
from brain_games.games.game_gcd.brain_gcd_qa import brain_gcd_qa
from brain_games.games.game_prime.brain_prime_qa import brain_prime_qa


def state_question_answer(game):
    right_answer = ''
    num_expression = ''
    if (game == 'brain_even'):
        num_expression, right_answer = brain_even_qa()
    elif (game == 'brain_calc'):
        num_expression, right_answer = gen_num_exp()
    elif (game == 'brain_gcd'):
        num_expression, right_answer = brain_gcd_qa()
    elif (game == 'brain_progression'):
        num_expression, right_answer = gen_prog()
    elif (game == 'brain_prime'):
        num_expression, right_answer = brain_prime_qa()
    return num_expression, right_answer
