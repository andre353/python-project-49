import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    name = name.capitalize()
    print(f'Hello, {name}!')
    return name
