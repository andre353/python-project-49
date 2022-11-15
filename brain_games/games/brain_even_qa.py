import random


def brain_even_qa():
    right_answer = ''
    num_expression = ''
    num_expression = str(random.randint(1, 100))
    if (int(num_expression) % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return num_expression, right_answer
