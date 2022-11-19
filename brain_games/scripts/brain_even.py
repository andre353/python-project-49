#!/usr/bin/env python3
from brain_games.games.brain_even import even
from brain_games.start_game import start_game


def main():
    # An entry point to launch brain_even game in the terminal
    start_game(even)


if __name__ == '__main__':
    main()
