# Name: Sonya Swiderski
# Prog Purpose: This program finds the gross pay, deductions, and net pay for an employee based on
# the number of hours they worked and their job category.
#   NOTE: All hourly pay rates are based on position
#       Cashier: $16.50
#       Stocker: $15.75
#       Janitor: $15.75
#       Maintenance: $19.50

import datetime
pay_rate = (16.50, 15.75, 15.75, 19.50,)
tax_deductions = (.12, .03, .062, .0145,)


# define global variables
employee_type = ["c", "s", "j", "m"]
num_hours = 0
gross_pay = 0
federal_income_tax = 0
state_income_tax = 0
social_security_tax = 0
medicare_tax = 0
net_pay = 0

############## define program functions ###############
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to add another employee? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False

def get_user_data():
    global employee_type, num_hours
    employee_type = str(input("Enter a c for Cashier, enter a s for Stocker, enter a j for Janitor, enter m for Maintenance: ").lower())
    num_hours = int(input("Number of hours worked: "))

def perform_calculations():
    global gross_pay, federal_income_tax, state_income_tax, social_security_tax, medicare_tax, net_pay
    if employee_type == 'c' :
        gross_pay = num_hours * pay_rate[0] 
    elif employee_type == 's' :
        gross_pay = num_hours * pay_rate[1]
    elif employee_type == 'j' :
        gross_pay = num_hours * pay_rate[2]
    elif employee_type == 'm' :
        gross_pay = num_hours * pay_rate[3]

    federal_income_tax = gross_pay * tax_deductions[0]
    state_income_tax = gross_pay * tax_deductions[1]
    social_security_tax = gross_pay * tax_deductions[2]
    medicare_tax = gross_pay * tax_deductions[3]
    net_pay = gross_pay + federal_income_tax + state_income_tax + social_security_tax + medicare_tax

def display_results():
    print('\n------------------------------------------------')
    print('Number of hours :      ' + str(num_hours))
    print('--------------------------------------------------')
    print('Gross Pay            $ ' + format(gross_pay,'8,.2f'))
    print('Federal Income Tax   $ ' + format(federal_income_tax,'8,.2f'))
    print('State Income Tax     $ ' + format(state_income_tax,'8,.2f'))
    print('Social Security Tax  $ ' + format(social_security_tax,'8,.2f'))
    print('Medicare tax         $ ' + format(medicare_tax,'8,.2f'))
    print('-------------------------------------------------')
    print('Net Pay              $ ' + format(net_pay,'8,.2f'))
    print('-------------------------------------------------')
    print(str(datetime.datetime.now()))
    
########## call on main program to execute ############
main()
