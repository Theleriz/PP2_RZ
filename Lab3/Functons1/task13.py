import random

def game():
    number = random.randint(1, 20)
    print("Hello! What is your name?")
    user_name = input()
    user_answer = -1
    number_of_gusses = 0
    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
    print("Take guess.")
    while user_answer != number:
        user_answer = int(input())
        if user_answer > number:
            print("Your guess is biger.")
            print("Take guess.")
            number_of_gusses += 1
        elif user_answer < number:
            print("Your guess is to low.")
            print("Take guess.")
            number_of_gusses += 1
        elif user_answer == number:
            print(f"Good job, {user_name}! You guessed my number in {number_of_gusses} guesses!")
            break

game()
