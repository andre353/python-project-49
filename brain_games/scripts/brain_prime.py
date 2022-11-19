#!/usr/bin/env python3
from brain_games.games.brain_prime import prime
from brain_games.start_game import start_game


def main():
    # An entry point to launch brain_prime game in the terminal
    start_game(prime)


if __name__ == '__main__':
    main()
