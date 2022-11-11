import prompt
import random
import math


def generate_rand_num():
    return random.randint(0, 100)


def generate_num_expression():
    first_num = generate_rand_num()
    second_num = generate_rand_num()
    list = ['+', '-', '*']
    operator = random.choice(list)
    result = dict()
    string = f'{first_num} {operator} {second_num}'
    result['str'] = string
    expr = string
    calculated_num = eval(expr)
    result['calculated_num'] = str(calculated_num)
    return result


def check_answer(right_res, user_ans):
    if (user_ans == right_res):
        print("Correct!")
        return True
    else:
        print(f"{user_ans} is wrong answer ;(. Correct answer was {right_res}.")
        return False


def check_user(game):
    right_answer = ''
    num_expression = ''
    if (game == 'brain_even'):
        num_expression = str(generate_rand_num())
        num = num_expression
        if (int(num) % 2 == 0):
            right_answer = 'yes'
        elif (int(num) % 2 != 0):
            right_answer = 'no'
    if (game == 'brain_calc'):
        result = generate_num_expression()
        num_expression, right_answer = result['str'], result['calculated_num']
    if (game == 'brain_gcd'):
        first_num = generate_rand_num()
        second_num = generate_rand_num()
        num_expression = f'{first_num} {second_num}'
        right_answer = str(math.gcd(first_num, second_num))
    print(f'Question: {num_expression}')
    user_answer = prompt.string('Your answer? ').lower()
    answer = check_answer(right_answer, user_answer)
    return answer