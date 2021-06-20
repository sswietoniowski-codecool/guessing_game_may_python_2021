import math
import random


def play_game(numbers, min_value, max_value):   
    def ask_user():
        return int(input(f"Enter an integer from {min_value} to {max_value}: "))

    for number in numbers:
        guessed_number = ask_user()
        while number != guessed_number:
            if guessed_number < number:
                print("guess is low")
                guessed_number = ask_user()
            elif guessed_number > number:
                print("guess is high")
                guessed_number = ask_user()
            else:
                break
        print("you guessed it!")


def prepare_random_numbers(count, min_value, max_value):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_value, max_value))
    return numbers


def main():
    numbers = prepare_random_numbers(10, 1, 99)
    play_game(numbers, 1, 99)

    numbers = prepare_random_numbers(10, 1, 49)
    play_game(numbers, 1, 49)


if __name__ == "__main__":
    main()
