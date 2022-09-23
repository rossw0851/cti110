#This program calculates and displays travel expenses
#9/22/2022
#CTI-110 P1HW2 - Travel Expense
#William "James" Ross
#Pseudocode (detail algorithm)

budget = 1200
print('Enter Budget:', budget)
destination= 'Asheville'
print('Enter your travel destination:', destination)
gas = 250
print('How much do you think you will spend on gas?', gas)
accomodation = 300
print('Approximately, how much will you need for accomodation/hotel?', accomodation)
food = 200
print('Last, how much do you need for food?', food)
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial budget:', budget)
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
print('Remaining Balance:', budget - gas - accomodation - food)
