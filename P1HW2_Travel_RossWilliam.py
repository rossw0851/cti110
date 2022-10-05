#This program calculates and displays travel expenses
#9/22/2022
#CTI-110 P1HW2 - Travel Expense
#William "James" Ross
#Pseudocode (detail algorithm)

budget = int(input('Enter Budget:'))
print(budget)
destination = input('Enter your travel destination:')
print(destination)
gas = int(input('How much do you think you will spend on gas?'))
print(gas)
accomodation = int(input('Approximately, how much will you need for accomodation/hotel?'))
print(accomodation)
food = int(input('Last, how much do you need for food?'))
print(food)
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial budget:', budget)
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
print('Remaining Balance:', budget - gas - accomodation - food)
