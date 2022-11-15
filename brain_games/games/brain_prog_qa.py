import random


def brain_prog_qa():
    gen_list = []
    num = random.randint(0, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    for _ in range(length):
        gen_list.append(num)
        num += step
    rand_index = random.randint(0, length - 1)
    hidden_num = str(gen_list[rand_index])
    list_to_str = ' '.join(str(i).replace(hidden_num, '..') for i in gen_list)
    return list_to_str, hidden_num
