import random


TASK = 'What is the result of the expression?'


def get_expression_and_solution():
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    expression = f'{first_num} {operator} {second_num}'
    solution = 0
    if operator == '+':
        solution = first_num + second_num
    elif operator == '-':
        solution = first_num - second_num
    elif operator == '*':
        solution = first_num * second_num
    solution = str(solution)
    return expression, solution
