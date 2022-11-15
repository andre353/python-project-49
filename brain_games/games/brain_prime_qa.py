from brain_games.games.generate_rand_num import generate_rand_num

def check_if_prime(num):
    if (num < 1):
        return
    right_answer = 'no'
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k += 1
    if (k <= 0):
        right_answer = 'yes'
    return right_answer

def brain_prime_qa():
    prep_num = generate_rand_num(1, 100)
    right_answer = check_if_prime(prep_num)
    num_expression = str(prep_num)
    return num_expression, right_answer
