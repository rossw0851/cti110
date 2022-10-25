# 10/25/2022
# Ross
#CTI-110 P2HW1 - Debugging
#Pseudocode (detail algorithm)

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print()
low = min(grades)
high = max(grades)
avg = sum(grades) / len(grades)
print('------------Results------------')
print('Lowest Grade:      ', min(grades))
print('Highest Grade:     ', max(grades))
print('Sum of Grades:     ', sum(grades))
print(f'Average:            {avg:.2f}')
print('------------------------------------------')

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
else:
    if avg > 80:
     print('Your grade is: B')
    else:
        if avg > 70:
            print('Your grade is: C')
        else:
            if avg > 60:
             print('Your grade is: D')
            else:
                print('Your grade is: F') # TO DO: finish this





