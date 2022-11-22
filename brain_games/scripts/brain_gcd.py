#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.start_game import start_game


def main():
    # An entry point to launch brain_gcd game in the terminal
    start_game(brain_gcd)


if __name__ == '__main__':
    main()
