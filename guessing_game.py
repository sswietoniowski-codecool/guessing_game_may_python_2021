import math
import random


def play_game(numbers):
    for i in range(10):
        guessed_number = int(input("Enter an integer from 1 to 99: "))
        while numbers[i] != guessed_number:
            if guessed_number < numbers[i]:
                print("guess is low")
                guessed_number = int(input("Enter an integer from 1 to 99: "))
            elif guessed_number > numbers[i]:
                print("guess is high")
                guessed_number = int(input("Enter an integer from 1 to 99: "))
            else:
                break
        print("you guessed it!")

def main():
    numbers = []
    for _ in range(10):
        numbers.append(random.randint(1, 99))
    play_game(numbers)
    

    b = []
    for _ in range(10):
        b.append(random.randint(1, 49))

    for i in range(10):
        g = int(input("Enter an integer from 1 to 49: "))
        while b[i] != g:
            if g < b[i]:
                print("guess is low")
                g = int(input("Enter an integer from 1 to 49: "))
            elif g > b[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 49: "))
            else:
                break
        print("you guessed it!")


if __name__ == "__main__":
    main()
