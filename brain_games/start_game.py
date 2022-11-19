import prompt
import random


GREETING_PHRASE = 'Welcome to the Brain Games!'
GREETING_QUESTION = "May I have your name? "
GREETING = "Hello"
ROUNDS_TOTAL = 3


def generate_rand_num(a=0, b=100):
    return random.randint(a, b)


def welcome_user():
    print(GREETING_PHRASE)
    name = prompt.string(GREETING_QUESTION)
    print(f'{GREETING}, {name}!')
    return name


def state_task(game):
    task = ''
    if (game == 'brain_even'):
        task = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif (game == 'brain_calc'):
        task = 'What is the result of the expression?'
    elif (game == 'brain_gcd'):
        task = 'Find the greatest common divisor of given numbers.'
    elif (game == 'brain_prog'):
        task = 'What number is missing in the progression?'
    elif (game == 'brain_prime'):
        task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


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
    (num_expression, right_answer) = game()[0]
    print(f'Question: {num_expression}')
    user_answer = prompt.string('Your answer? ')
    answer = check_answer(right_answer, user_answer)
    return answer


def win_count(game):
    round = 0
    win_count = 0
    while round < ROUNDS_TOTAL:
        answer = check_user(game)
        if (answer):
            win_count += 1
        else:
            break
        round += 1
    return win_count


def output_result(game):
    count = win_count(game)
    if count == ROUNDS_TOTAL:
        return True
    else:
        return False


def start_game(game):
    name = welcome_user()
    game_name = game()[1]
    task = state_task(game_name)
    print(task)
    if (output_result(game)):
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
