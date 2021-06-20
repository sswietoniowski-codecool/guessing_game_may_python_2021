import math
import random


def play_game(numbers, min_value, max_value):
    def ask_user():
        return int(input(f"Enter an integer from {min_value} to {max_value}: "))

    for number in numbers:
        guessed_number = 0
        while number != guessed_number:
            guessed_number = ask_user()
            if guessed_number < number:
                print("guess is low")
            elif guessed_number > number:
                print("guess is high")
        print("you guessed it!")


def prepare_random_numbers(count, min_value, max_value):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_value, max_value))
    return numbers


def game(count, min_value, max_value):
    numbers = prepare_random_numbers(count, min_value, max_value)
    play_game(numbers, min_value, max_value)


def main():
    game(10, 1, 99)
    game(10, 1, 49)


if __name__ == "__main__":
    main()
