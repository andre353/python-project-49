import prompt
from brain_games.games.consts import GREETING_PHRASE


def welcome_user():
    print(GREETING_PHRASE)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
