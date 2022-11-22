from brain_games.start_game import generate_rand_num


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


def module_func():
    answers = ["no", "yes"]
    prep_num = generate_rand_num(1, 100)
    solution = answers[is_prime(prep_num)]
    num_expression = str(prep_num)
    return num_expression, solution
