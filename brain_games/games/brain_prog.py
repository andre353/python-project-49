import random
from brain_games.start_game import generate_rand_num


def prog():
    game_name = 'brain_prog'
    gen_list = []
    num = generate_rand_num()
    step = generate_rand_num(1, 10)
    length = generate_rand_num(5, 10)
    for _ in range(length):
        gen_list.append(num)
        num += step
    rand_index = random.randint(0, length - 1)
    hidden_num = str(gen_list[rand_index])
    list_to_str = ' '.join(str(i).replace(hidden_num, '..') for i in gen_list)
    return (list_to_str, hidden_num), game_name
