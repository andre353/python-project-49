def state_task(game):
    task = ''
    if (game == 'brain_even'):
        task = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif (game == 'brain_calc'):
        task = 'What is the result of the expression?'
    elif (game == 'brain_gcd'):
        task = 'Find the greatest common divisor of given numbers.'
    elif (game == 'brain_progression'):
        task = 'What number is missing in the progression?'
    elif (game == 'brain_prime'):
        task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task
