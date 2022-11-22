#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games.start_game import start_game


def main():
    # An entry point to launch brain_prime game in the terminal
    start_game(brain_prime)


if __name__ == '__main__':
    main()
