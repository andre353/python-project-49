import prompt
import random


GREETING_PHRASE = 'Welcome to the Brain Games!'
GREETING_QUESTION = "May I have your name? "
GREETING = "Hello"
ROUNDS_TOTAL = 3


def generate_rand_num(a=0, b=100):
    return random.randint(a, b)


def start_game(game):
    print(GREETING_PHRASE)
    name = prompt.string(GREETING_QUESTION)
    print(f'{GREETING}, {name}!')

    task = game()[1]
    print(task)

    round = 0
    win_count = 0
    while round < ROUNDS_TOTAL:
        num_expression, solution = game()[0]
        print(f'Question: {num_expression}')
        u_anw = prompt.string('Your answer? ')
        if (u_anw == solution):
            print("Correct!")
            win_count += 1
        else:
            print(f"{u_anw} is wrong answer ;(. Correct answer was {solution}.")
            break
        round += 1

    if win_count == ROUNDS_TOTAL:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
