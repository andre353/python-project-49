from brain_games.games.win_count import win_count


def output_result(game):
    count = win_count(game)
    if count == 3:
        return True
    else:
        return False
