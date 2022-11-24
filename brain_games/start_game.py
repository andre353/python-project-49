import prompt


ROUNDS_TOTAL = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"{'Hello'}, {name}!")
    print(game.TASK)
    count = 0
    while count < ROUNDS_TOTAL:
        num_expression, solution = game.get_expression_and_solution()
        print(f"Question: {num_expression}")
        user_answer = prompt.string('Your answer? ')
        if user_answer == solution:
            print('Correct!')
            count += 1
        else:
            print(
                f"{user_answer} is wrong answer ;(. "
                f"Correct answer was {solution}."
            )
            break
    if count == ROUNDS_TOTAL:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let\'s try again, {name}!")
