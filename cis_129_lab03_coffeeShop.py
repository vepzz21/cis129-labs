'''
Emmanuel Piña-Zelinger
CIS129
Module 3: Lab
The purpose of this lab is to create an interactive text-based Coffee
Shop simulator that calculates a receipt based on how many items the 
user wants to order.
'''


def coffeeShop():
    '''
    This function obtains menu-input from cusstomer, calculates pricing
    based on input, and generates a receipt, containing the total of 
    what the customer purchased.
    Also, this function follows the IPO procedure. 
    '''
    #below is the input.
    coffee_request = int(input("Hi! Enter desired cups of coffee: "))
    coffee_order = str(coffee_request)
    muffin_request = int(input("Enter desired number of muffins: "))
    muffin_order = str(muffin_request)

    #below is the processing.
    coffee_calculation = coffee_request * 5
    formatted_coffee_calculation = "{:.2f}".format(coffee_calculation)
    muffin_calculation = muffin_request * 4
    formatted_muffin_calculation = "{:.2f}".format(muffin_calculation)
    tax_calculation = float(((coffee_calculation + muffin_calculation)*0.06))
    tax = round(tax_calculation,2)
    total = float((coffee_calculation+muffin_calculation+tax))

    #below is the output. 
    receipt = "***************************************\
\nMy Coffee and Muffin Shop\
\nNumber of coffees bought?\
\n"+str(coffee_request)+"\nNumber of muffins bought?\
\n"+str(muffin_request)+"\n***************************************\
\n\
\n***************************************\
\nMy Coffee and Muffin Shop Receipt\
\n1 Coffee at $5 each: $"+str(formatted_coffee_calculation)+"\
\n2 Muffins at $4 each: $"+str(formatted_muffin_calculation)+"\
\n6% tax: $"+str(tax)+"\
\n---------\
\nTotal: $"+str(total)+"\
\n***************************************"
    print(receipt)

coffeeShop()
