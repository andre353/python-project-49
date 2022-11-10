import prompt
import random


def generate_rand_num():
    return random.randint(0, 100)


def check_answer(num, user_answer):
    if (num % 2 == 0):
        if (user_answer == 'yes'):
            print("Correct!")
            return True
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False
    if (num % 2 != 0):
        if (user_answer == 'no'):
            print("Correct!")
            return True
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False


def output_result():
    round = 0
    win_count = 0
    answer = False
    while round < 3:
        ran_num = generate_rand_num()
        print(f'Question: {ran_num}')
        user_answer = prompt.string('Your answer? ')
        user_answer = user_answer.lower()
        answer = check_answer(ran_num, user_answer)
        if (answer):
            win_count += 1
        else:
            win_count -= 1
        round += 1
    if win_count == 3:
        return True
    else:
        return False


def even_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if (output_result()):
        return (f'Congratulations, {name}')
    else:
        return (f'Let\'s try again, {name}!')
