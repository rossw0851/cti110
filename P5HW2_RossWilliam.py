#This program gives simple math quizzes.
#11/22/2022
#CTI-110 P5HW2 - Math Quiz
#William "James" Ross
#Pseudocode (detail algorithm)

import random
def menu():
    print('Welcome to Math Quiz')
    print()
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()
    choose = int(input('Please choose one of the menu options:'))

    if choose == '1':
        add()

    elif choose == '2':
        subtract()

    elif choose == '3':
        exit
    else:
        print('ERROR, please enter only numbers: 1, 2, or 3.')

def add():
    num_1 = random.randint(1,99)
    num_2 = random.randint(1,99)
    correct = num_1 + num_2
    print(' ', num_1)
    print('+', num_2)
    answer = int(input('Enter answer.\n'))
    if correct == answer:
        print('Congradulations!!! your answer is correct..:')
        menu()
    elif answer < correct:
        print('Sorry, guess is too low.')
        print()
        answer = int(input('try again:'))
    elif answer > correct:
        print('Sorry, guess is too high.')
        print()
        answer = int(input('try again:'))
        guesses += 1
        print('Number of guesses:', guesses)

def subtract():
    num_1 = random.randint(1,99)
    num_2 = random.randint(1,99)
    correct = num_1 - num_2
    print(' ', num_1)
    print('-', num_2)
    answer = int(input('Enter answer.\n'))
    if correct == answer:
        print('Congradulations!!! your answer is correct..:')
        menu()
    elif answer < correct:
        print('Sorry, guess is too low.')
        print()
        answer = int(input('try again:'))
    elif answer > correct:
        print('Sorry, guess is too high.')
        print()
        answer = int(input('try again:'))
    guesses += 1
    print('Number of guesses:', guesses) 
menu()
add()
subtract()
