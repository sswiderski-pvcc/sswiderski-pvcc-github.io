# Name: Sonya Swiderski
# Prog Purpose: This program finds the cost of pizza
#   NOTE: All pizza prices are based on size
#       Small pizza: $9.99
#       Medium pizza: $12.99
#       Large pizza: $14.99
#       Extra large pizza: $17.99
#       Sales tax rate: 5.5%

import datetime
# define tax rate and prices
SALES_TAX_RATE = .055
PIZZA_S = 9.99
PIZZA_M = 12.99
PIZZA_L = 14.99
PIZZA_X = 17.99

# define global variables
size = ["s", "m", "l", "x"]
num_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ###############
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to add to your order? (Y/N): ")
        if yesno.upper() != "Y":
            another_pizza = False

def get_user_data():
    global size, num_pizza
    size = str(input("Enter a s for small pizza, enter a m for medium pizza, enter a l for large pizza, enter x for extra large pizza: ").lower())
    num_pizza = int(input("Number of pizzas: "))

def perform_calculations():
    global subtotal, sales_tax, total
    if size == 's' :
        subtotal = num_pizza * PIZZA_S
    elif size == 'm' :
        subtotal = num_pizza * PIZZA_M
    elif size == 'l' :
        subtotal = num_pizza * PIZZA_L
    elif size == 'x' :
        subtotal = num_pizza * PIZZA_X

    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------')
    print('**** PALERMO PIZZA ****')
    print('Best pizza in the state')
    print('------------------------')
    print('Pizza        $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('------------------------')
    print(str(datetime.datetime.now()))
    
########## call on main program to execute ############
main()
