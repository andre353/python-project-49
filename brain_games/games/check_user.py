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
    string = f'{first_num} {operator} {second_num}'
    expr = string
    calculated_num = eval(expr)
    return string, str(calculated_num)


def generate_progression():
    gen_list = []
    num = generate_rand_num()
    step = random.randint(0, 10)
    length = random.randint(5, 10)
    for _ in range(length):
        gen_list.append(num)
        num += step
    rand_index = random.randint(0, length - 1)
    hidden_num = str(gen_list[rand_index])
    list_to_str = ' '.join(str(i).replace(hidden_num, '..') for i in gen_list)
    return list_to_str, hidden_num


def check_answer(right_res, user_ans):
    if (user_ans == right_res):
        print("Correct!")
        return True
    else:
        print(f"{user_ans} is wrong answer ;(. Correct answer was {right_res}.")
        return False


def state_question_answer(game):
    right_answer = ''
    num_expression = ''
    random_num = generate_rand_num()
    if (game == 'brain_even'):
        num_expression = str(random_num)
        if (int(num_expression) % 2 == 0):
            right_answer = 'yes'
        elif (int(num_expression) % 2 != 0):
            right_answer = 'no'
    elif (game == 'brain_calc'):
        num_expression, right_answer = generate_num_expression()
    elif (game == 'brain_gcd'):
        first_num = random_num
        second_num = generate_rand_num()
        num_expression = f'{first_num} {second_num}'
        right_answer = str(math.gcd(first_num, second_num))
    elif (game == 'brain_progression'):
        num_expression, right_answer = generate_progression()
    return num_expression, right_answer


def check_user(game):
    num_expression, right_answer = state_question_answer(game)
    print(f'Question: {num_expression}')
    user_answer = prompt.string('Your answer? ').lower()
    answer = check_answer(right_answer, user_answer)
    return answer
