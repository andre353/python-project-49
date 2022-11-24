import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if (num < 1):
        return
    right_answer = False
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k += 1
    if (k <= 0):
        right_answer = True
    return right_answer


def get_expression_and_solution():
    prep_num = random.randint(1, 100)
    solution = 'yes' if is_prime(prep_num) else 'no'
    expression = str(prep_num)
    return expression, solution
