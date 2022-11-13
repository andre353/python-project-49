import prompt
from brain_games.games.check_answer import check_answer
from brain_games.games.state_question_answer import state_question_answer


def check_user(game):
    num_expression, right_answer = state_question_answer(game)
    print(f'Question: {num_expression}')
    user_answer = prompt.string('Your answer? ')
    answer = check_answer(right_answer, user_answer)
    return answer
