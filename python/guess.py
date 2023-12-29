from random import randrange

user_input = ""
comp_guess_number = 0

while user_input != 'exit':
    user_input = int(input("Enter any number from 1 to 10\n"))
    print(f"Your guess number is {user_input}\n")
    comp_guess_number = randrange(1, 11) 
    print(f"Computer guess number is: {comp_guess_number}")
    if user_input == comp_guess_number:
        print(f"YOU WON! 🎊")
        user_input = 'exit'