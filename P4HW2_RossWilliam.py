#CTI-110
#P4HW2 - Salary Calculator
#William "James" Ross
#11/14/2022
#Pseudocode (detail algorithm)

employee_name = input("Enter employee's name or " '"None"' ' to terminate:')

employee_num = 1
overtime_total = 0
reg_total = 0
gross_total = 0

while employee_name != 'None':
    hours_worked = float(input('How many hours did' + employee_name + ' worked?'))
    pay_rate = float(input("What is" + employee_name + "'s pay rate?"))

    if hours_worked <= 40:
        overtime_hours = 0
        regPay = hours_worked * pay_rate
    else:
        hours_worked > 40
        overtime_hours = hours_worked - 40
        regPay = 40 * pay_rate
    if overtime_hours == 0:
        overpay = 0
    else:
        overtime_rate = pay_rate * 1.5
        overpay = overtime_rate * overtime_hours
    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate
    else:
        hours_worked > 40
        gross_pay = ((hours_worked - 40) * pay_rate * 1.5) + pay_rate * 40
    print()
    print('Employee name:', employee_name)
    print()
    print('Hours Worked   Pay Rate    Overtime    Overtime Pay        RegHour Pay         Gross Pay')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12}{overpay:<20}${regPay:<20.2f}${gross_pay:.2f}')
    print()
    print()

    employee_name = input("Enter employee's name or " '"None"' ' to terminate:')

    employee_num += 1
    
else:
    print('Total number of employees entered:{}'.format(employee_num - 1))
    print('Total amount payed for overtime: ${:.2f}'.format(overtime_total))
    print('Total amount payed for regular hours: ${:.2f}'.format(reg_total))
    print('Total amount payed in gross ${:.2f}'.format(gross_total))
