from brain_games.games.game_prime.check_if_prime import check_if_prime
from brain_games.games.generate_rand_num import generate_rand_num


def brain_prime_qa():
    prep_num = generate_rand_num(1, 100)
    right_answer = check_if_prime(prep_num)
    num_expression = str(prep_num)
    return num_expression, right_answer
