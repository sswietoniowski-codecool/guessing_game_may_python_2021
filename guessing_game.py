import math
import random


def play_game(numbers, min_value, max_value):
    for i in range(10):
        guessed_number = int(
            input(f"Enter an integer from {min_value} to {max_value}: "))
        while numbers[i] != guessed_number:
            if guessed_number < numbers[i]:
                print("guess is low")
                guessed_number = int(
                    input(f"Enter an integer from {min_value} to {max_value}: "))
            elif guessed_number > numbers[i]:
                print("guess is high")
                guessed_number = int(
                    input(f"Enter an integer from {min_value} to {max_value}: "))
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
