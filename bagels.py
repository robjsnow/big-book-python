import random
game_over = False
while (not game_over):
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.''')
    digit_1 = str(random.randint(0,9))
    digit_2 = str(random.randint(0,9))
    digit_3 = str(random.randint(0,9))

    computer_answer = f'{digit_1}{digit_2}{digit_3}'
    max_tries = 10
    current_guess = 0
    print("I am thinking of a 3 digit number. Try to guess what it is.\n")
    
    while (not game_over):
        current_guess = current_guess + 1
        if current_guess == max_tries + 1:
            print("You lose.")
            game_over = True
            break;
        else:
            user_answer = input(f"Guess #{current_guess}\n>")
        if user_answer == computer_answer:
            print("You got it!")
            game_over = True
            break

        elif user_answer[0] in computer_answer or user_answer[1] in computer_answer or user_answer[2] in computer_answer:
            for index, x in enumerate(computer_answer):
                if x == user_answer[index]:
                   print("Fermi")
                else:
                    if user_answer[index] in computer_answer:
                        print("Pico")
        else:
            print("Bagels")

    play_again = input("Do you want to play again? (yes or no)\n").lower()
    if play_again == "yes":
        game_over = False
    else:
        print("Thanks for playing!")
        