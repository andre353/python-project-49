import prompt
from brain_games.games.brain_prog_qa import brain_prog_qa
from brain_games.games.brain_calc_qa import brain_calc_qa
from brain_games.games.brain_even_qa import brain_even_qa
from brain_games.games.brain_gcd_qa import brain_gcd_qa
from brain_games.games.brain_prime_qa import brain_prime_qa


def state_question_answer(game):
    right_answer = ''
    num_expression = ''
    if (game == 'brain_even'):
        num_expression, right_answer = brain_even_qa()
    elif (game == 'brain_calc'):
        num_expression, right_answer = brain_calc_qa()
    elif (game == 'brain_gcd'):
        num_expression, right_answer = brain_gcd_qa()
    elif (game == 'brain_progression'):
        num_expression, right_answer = brain_prog_qa()
    elif (game == 'brain_prime'):
        num_expression, right_answer = brain_prime_qa()
    return num_expression, right_answer


def check_answer(right_res, user_ans):
    answer = False
    if (user_ans == right_res):
        print("Correct!")
        answer = True
    else:
        print(f"{user_ans} is wrong answer ;(. Correct answer was {right_res}.")
        answer = False
    return answer


def check_user(game):
    num_expression, right_answer = state_question_answer(game)
    print(f'Question: {num_expression}')
    user_answer = prompt.string('Your answer? ')
    answer = check_answer(right_answer, user_answer)
    return answer
