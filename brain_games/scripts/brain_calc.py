#!/usr/bin/env python3
from brain_games.games.brain_calc import calc
from brain_games.start_game import start_game


def main():
    # An entry point to launch brain_calc game in the terminal
    start_game(calc)


if __name__ == '__main__':
    main()
