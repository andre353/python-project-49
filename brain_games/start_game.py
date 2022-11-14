from brain_games.games.output_result import output_result
from brain_games.games.welcome_user import welcome_user
from brain_games.games.state_task import state_task


def start_game(game):
    name = welcome_user()
    task = state_task(game)
    print(task)
    if (output_result(game)):
        return (f'Congratulations, {name}!')
    else:
        return (f'Let\'s try again, {name}!')
