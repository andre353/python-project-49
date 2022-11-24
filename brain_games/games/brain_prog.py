import random


TASK = 'What number is missing in the progression?'


def get_expression_and_solution():
    progression = []
    num = random.randint(0, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    for _ in range(length):
        progression.append(num)
        num += step
    rand_index = random.randint(0, length - 1)
    solution = str(progression[rand_index])
    expression = ' '.join(str(i).replace(solution, '..') for i in progression)
    return expression, solution
