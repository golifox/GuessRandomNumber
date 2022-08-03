import os
import random
from xml.dom import ValidationErr

clear = lambda: os.system('cls')

def start_message():
    print('Computer was create new random number (0-10). \nWould you guess it? (Y/N)')
    return input()

def input_message():
    print ('Input your number: ')
    return input()

def compare_numbers (num1: int, num2: int):
    if num1 == num2:
        print("Congradulations!\nYou guessed right number!\n")
        return 1
    else:
        print("You doesn`t guessed right!")
        return 0

def validate_number(number):
    valid = False
    while not valid:
        try:
            number = int(number)
        except:
            print('Incorrect input!')
        valid = True

def test():
    number = random.randint(0,10)
    print (number)
    return number
   

user_choice = start_message()

while (user_choice.capitalize() == 'Y'):
    ##test_block
    computer_number = test()

    user_number = validate_number (input_message()) ##get user number and validate it to INT
    
    ##computer_number = random.randint(0,10) ##generate random number

    while not compare_numbers(computer_number, user_number): ##compare and while not equals get user`s another number`
        user_number = validate_number(input_message())            

    user_choice = start_message()

print('Exiting...')