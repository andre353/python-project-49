#!/usr/bin/env python3
from brain_games.welcome_user import welcome_user
from brain_games.even_check import even_check


def main():
    print('Welcome to the Brain Games!')
    user = welcome_user()
    print(even_check(user))


if __name__ == '__main__':
    main()
