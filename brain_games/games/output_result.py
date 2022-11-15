from brain_games.games.check_user import check_user
from brain_games.games.consts import ROUNDS_TOTAL


def win_count(game):
    round = 0
    win_count = 0
    while round < ROUNDS_TOTAL:
        answer = check_user(game)
        if (answer):
            win_count += 1
        else:
            break
        round += 1
    return win_count


def output_result(game):
    count = win_count(game)
    if count == 3:
        return True
    else:
        return False
