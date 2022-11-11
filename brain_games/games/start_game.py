from brain_games.games.output_result import output_result
from brain_games.games.welcome_user import welcome_user


def start_game(game):
    name = welcome_user()
    task = ''
    if (game == 'brain_even'):
        task = 'Answer "yes" if the number is even, otherwise answer "no".'
    if (game == 'brain_calc'):
        task = 'What is the result of the expression?'
    if (game == 'brain_gcd'):
        task = 'Find the greatest common divisor of given numbers.'
    print(task)
    if (output_result(game)):
        return (f'Congratulations, {name}')
    else:
        return (f'Let\'s try again, {name}!')
