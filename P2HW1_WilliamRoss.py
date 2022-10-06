#This program calculates and displays travel expenses
#10/5/2022
#CTI-110 P2HW1 - Travel
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
print('Location:         ', destination)
print('Initial Budget:    ', f'${budget:.1f}')
print('Fuel:              ', f'${gas:.1f}')
print('Accomodation:      ', f'${accomodation:.1f}')
print('Food:              ', f'${food:.1f}')
print('---------------------------------------')
print()
print('Remaining Balance: ', f'${budget - gas - accomodation - food:.1f}')
