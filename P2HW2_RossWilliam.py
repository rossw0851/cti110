#CTI-110
#P2HW2 - List
#William "James" Ross
#10/13/2022
#Pseudocode (detail algorithm)

module_1 = float(input('Enter grade for Module 1:'))
module_2 = float(input('Enter grade for Module 2:'))
module_3 = float(input('Enter grade for Module 3:'))
module_4 = float(input('Enter grade for Module 4:'))
module_5 = float(input('Enter grade for Module 5:'))
module_6 = float(input('Enter grade for Module 6:'))
print()
grades = [module_1, module_2, module_3, module_4, module_5, module_6]
print('------------Results------------')
print('Lowest Grade:      ', min(grades))
print('Highest Grade:     ', max(grades))
print('Sum of Grades:     ', sum(grades))
avg_grades = (module_1 + module_2 + module_3 + module_4 + module_5 + module_6) /6
print(f'Average grades:     {avg_grades:.2f}')
print('----------------------------------------')
