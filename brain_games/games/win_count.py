from brain_games.games.check_user import check_user


def win_count(game):
    round = 0
    win_count = 0
    while round < 3:
        answer = check_user(game)
        if (answer):
            win_count += 1
        else:
            win_count -= 1
        round += 1
    return win_count