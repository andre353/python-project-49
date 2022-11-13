def check_if_prime(num):
    right_answer = 'no'
    k = 0
    if (num > 1):
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                k += 1
        if (k <= 0):
            right_answer = 'yes'
    return right_answer
