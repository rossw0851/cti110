#CTI-110
#P3HW2 - Salary
#William "James" Ross
#10/27/2022
#Pseudocode (detail algorithm)

employee_name = input("Enter employee's name:")
hours_worked = float(input('Enter number of hours worked:'))
pay_rate = float(input("Enter employee's pay rate:"))
if hours_worked <= 40:
    overtime_hours = 0
elif hours_worked > 40:
    overtime_hours = hours_worked - 40

overtime_rate = pay_rate * 1.5
overtime_pay = overtime_rate * overtime_hours
    
reg_pay = 40 * pay_rate

if hours_worked <= 40:
    gross_pay = hours_worked * pay_rate
elif hours_worked > 40:
    gross_pay = ((hours_worked - 40) * pay_rate * 1.5) + pay_rate * 40 
print('-------------------------------------')
print('Employee name:', employee_name)
print()
print('Hours Worked        Pay Rate        OverTime        OverTime Pay        RegHour Pay        Gross Pay')
print('--------------------------------------------------------------------------------------------------------------')
print(f'{hours_worked:<20}{pay_rate:<16}{overtime_hours:<16}{overtime_pay:<20}${reg_pay:<19.2f}${gross_pay}')
